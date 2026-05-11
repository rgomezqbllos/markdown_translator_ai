from flask import Flask, render_template, request, jsonify, Response
import os
import json
import subprocess
import platform
from dotenv import load_dotenv

load_dotenv()

from core.ai_engine import AIEngine
from core.glossary_manager import GlossaryManager
from core.markdown_translator import MarkdownTranslator

app = Flask(__name__)

# Instancias globales lazy
engine = None
gm = GlossaryManager("glosario.json")
stop_translation = False

SUPPORTED_MODELS = {
    "qwen2.5_7b": {
        "name": "Qwen 2.5 (7B) - Mejor Opción Multilingüe",
        "repo_id": "bartowski/Qwen2.5-7B-Instruct-GGUF",
        "filename": "Qwen2.5-7B-Instruct-Q4_K_M.gguf"
    },
    "llama3_8b": {
        "name": "Llama 3.1 (8B) - Alta Calidad",
        "repo_id": "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
        "filename": "Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"
    },
    "gemma2_9b": {
        "name": "Gemma 2 (9B)",
        "repo_id": "bartowski/gemma-2-9b-it-GGUF",
        "filename": "gemma-2-9b-it-Q4_K_M.gguf"
    },
    "gemma_2b": {
        "name": "Gemma 2 (2B) - Ultra Rápido",
        "repo_id": "bartowski/gemma-2-2b-it-GGUF",
        "filename": "gemma-2-2b-it-Q4_K_M.gguf"
    },
    "command_r_lite": {
        "name": "Command R (35B - Q3) - Límite de 16GB",
        "repo_id": "bartowski/c4ai-command-r-v01-GGUF",
        "filename": "c4ai-command-r-v01-Q3_K_M.gguf"
    },
    "mistral_7b": {
        "name": "Mistral v0.3 (7B)",
        "repo_id": "MaziyarPanahi/Mistral-7B-Instruct-v0.3-GGUF",
        "filename": "Mistral-7B-Instruct-v0.3.Q4_K_M.gguf"
    }
}

def get_engine(model_id="qwen2.5_7b"):
    global engine
    if engine is None:
        engine = AIEngine()
        
    model_info = SUPPORTED_MODELS.get(model_id, SUPPORTED_MODELS["qwen2.5_7b"])
    engine.load_model(model_repo=model_info["repo_id"], model_filename=model_info["filename"])
    return engine

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/models")
def get_models():
    return jsonify({
        k: {"name": v["name"]} 
        for k, v in SUPPORTED_MODELS.items()
    })

@app.route("/api/stop", methods=["POST"])
def stop():
    global stop_translation
    stop_translation = True
    return jsonify({"status": "Deteniendo..."})

@app.route("/api/languages")
def get_languages():
    langs = list(gm.glossary.get("language_instructions", {}).keys())
    if not langs:
        langs = ["es", "en", "pt", "fr"]
    return jsonify(langs)

@app.route("/api/browse_folder", methods=["POST"])
def browse_folder():
    """Abre el explorador de archivos nativo del sistema operativo para seleccionar una carpeta."""
    system = platform.system()
    folder = ""
    try:
        if system == "Darwin": # macOS
            cmd = ['osascript', '-e', 'tell application (path to frontmost application as text) to set myFolder to choose folder', '-e', 'POSIX path of myFolder']
            result = subprocess.run(cmd, capture_output=True, text=True)
            folder = result.stdout.strip()
        elif system == "Windows":
            # Usar tkinter para el diálogo de selección en Windows (más estable que PowerShell)
            cmd = ['python', '-c', "import tkinter as tk, tkinter.filedialog as fd; root=tk.Tk(); root.attributes('-topmost', True); root.withdraw(); print(fd.askdirectory())"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            folder = result.stdout.strip()
        elif system == "Linux":
            cmd = ['zenity', '--file-selection', '--directory']
            result = subprocess.run(cmd, capture_output=True, text=True)
            folder = result.stdout.strip()
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
    return jsonify({"folder": folder})

@app.route("/api/translate", methods=["POST"])
def translate():
    global stop_translation
    stop_translation = False
    
    data = request.json
    input_dir = data.get("input_dir")
    output_dir = data.get("output_dir")
    source_lang = data.get("source_lang")
    target_lang = data.get("target_lang")
    model_id = data.get("model_id", "llama3_8b")
    
    if not all([input_dir, output_dir, source_lang, target_lang]):
        return jsonify({"error": "Faltan parámetros requeridos."}), 400
        
    if not os.path.exists(input_dir):
        return jsonify({"error": f"La ruta de entrada '{input_dir}' no existe."}), 400

    def generate_events():
        global stop_translation
        def check_cancel():
            return stop_translation
            
        yield "data: [INFO] Sincronizando archivos en la nube (iCloud, OneDrive, etc)...\n\n"
        
        # Forzar descarga de iCloud en Mac
        if platform.system() == "Darwin":
            subprocess.run(["brctl", "download", input_dir], capture_output=True)
            
        if stop_translation:
            yield "data: [WARN] TRADUCCIÓN CANCELADA POR EL USUARIO.\n\n"
            return
            
        yield f"data: [INFO] Iniciando motor de IA con modelo {SUPPORTED_MODELS.get(model_id, {}).get('name', 'Default')} (puede tomar unos segundos si es nuevo)...\n\n"
        try:
            eng = get_engine(model_id)
            translator = MarkdownTranslator(eng, gm)
            yield f"data: [INFO] Motor IA listo. Analizando directorio: {input_dir}\n\n"
            
            # Buscar archivos iterando, esperando descargas si es necesario
            files_to_translate = []
            for root, _, files in os.walk(input_dir):
                for file in files:
                    if file.endswith('.md') or file.endswith('.md.icloud'):
                        files_to_translate.append(os.path.join(root, file))
            
            if not files_to_translate:
                yield "data: [WARN] No se encontraron archivos Markdown (.md) en el directorio de entrada.\n\n"
            
            for index, input_path in enumerate(files_to_translate):
                if stop_translation:
                    yield "data: [WARN] TRADUCCIÓN CANCELADA POR EL USUARIO.\n\n"
                    break
                    
                # Si es un archivo de iCloud no descargado, esperamos a que se descargue
                if input_path.endswith('.icloud'):
                    real_path = input_path.replace('.icloud', '')
                    # Quitar el punto inicial de iCloud (ej: .archivo.md.icloud -> archivo.md)
                    dir_name, file_name = os.path.split(real_path)
                    if file_name.startswith('.'):
                        real_path = os.path.join(dir_name, file_name[1:])
                    
                    yield f"data: [INFO] Esperando descarga de la nube para: {os.path.basename(real_path)}...\n\n"
                    # Llamar a brctl específicamente para este
                    subprocess.run(["brctl", "download", input_path], capture_output=True)
                    import time
                    wait_time = 0
                    while not os.path.exists(real_path) and wait_time < 30:
                        if stop_translation: break
                        time.sleep(1)
                        wait_time += 1
                    input_path = real_path

                if stop_translation:
                    yield "data: [WARN] TRADUCCIÓN CANCELADA POR EL USUARIO.\n\n"
                    break

                rel_path = os.path.relpath(input_path, input_dir)
                
                # Traducir el nombre del archivo / carpetas
                yield f"data: [INFO] Traduciendo nombre del archivo: {os.path.basename(rel_path)}...\n\n"
                translated_rel_path = translator.translate_path(rel_path, source_lang, target_lang)
                output_path = os.path.join(output_dir, translated_rel_path)
                
                yield f"data: [PROCESANDO] {rel_path} -> {translated_rel_path} ({index+1}/{len(files_to_translate)})\n\n"
                
                translator.translate_file(input_path, output_path, source_lang, target_lang, cancel_callback=check_cancel)
                
                if stop_translation:
                    yield "data: [WARN] TRADUCCIÓN CANCELADA POR EL USUARIO.\n\n"
                    break
                    
                yield f"data: [OK] {translated_rel_path} guardado con éxito.\n\n"
                
            if not stop_translation:
                yield "data: TRADUCCION_FINALIZADA\n\n"
        except Exception as e:
            yield f"data: [ERROR] Ocurrió un fallo: {str(e)}\n\n"
            
    return Response(generate_events(), mimetype='text/event-stream')

if __name__ == "__main__":
    print("Iniciando aplicación GoalBus Markdown Translator...")
    print("Abre http://127.0.0.1:5050 en tu navegador.")
    app.run(debug=True, port=5050, use_reloader=False)
