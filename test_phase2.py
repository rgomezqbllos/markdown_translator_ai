import sys
import os
from core.glossary_manager import GlossaryManager
from core.ai_engine import AIEngine
from core.markdown_translator import MarkdownTranslator

def main():
    print("--- Probando Traductor de Markdown (Fase 2) ---")
    
    source_lang = "es"
    target_lang = "en"
    
    input_dir = "test_docs"
    output_dir = "test_docs_translated"
    
    # 1. Cargar Glosario
    gm = GlossaryManager("glosario.json")
    
    # 2. Inicializar Motor IA
    print("Iniciando carga del modelo de IA...")
    engine = AIEngine()
    try:
        engine.load_model()
    except Exception as e:
        print(f"Error cargando el modelo: {e}")
        sys.exit(1)
        
    # 3. Inicializar Traductor Markdown
    md_translator = MarkdownTranslator(engine, gm)
    
    print(f"\nIniciando traducción masiva de la carpeta: {input_dir}")
    print(f"Idioma Origen: {source_lang} -> Idioma Destino: {target_lang}")
    
    # Asegurar que existe el dir de input
    if not os.path.exists(input_dir):
        print(f"La carpeta '{input_dir}' no existe. Asegúrate de crearla y poner archivos .md dentro.")
        sys.exit(1)
        
    # 4. Procesar directorio
    md_translator.translate_directory(input_dir, output_dir, source_lang, target_lang)
    
    print("\n--- ¡Traducción Completada! ---")
    print(f"Revisa la carpeta: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    main()
