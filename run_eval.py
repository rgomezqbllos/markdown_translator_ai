import os
import json
import time
from core.ai_engine import AIEngine
from core.glossary_manager import GlossaryManager
from core.markdown_translator import MarkdownTranslator
from app import SUPPORTED_MODELS

# --- CONFIGURACIÓN DE LA PRUEBA v4 (FINAL) ---
# Gemma 2B eliminado: confunde idiomas (hebreo en IT, portugués en DE)
# Llama 3.1 eliminado: alucinación masiva en frontmatter (inventa cientos de líneas)
# Motor final: Qwen 2.5 (7B) — mejor balance calidad/consistencia
MODELS_TO_TEST = [
    "qwen2.5_7b",     # Motor final seleccionado
]
LANGUAGES = ["en", "pt-br", "pt-pt", "fr", "de", "it", "ar"]
FILES_TO_TEST = [
    "P1_Entendendo_o_papel_do_planejador_e_o_fluxo_end_to_end_AI.md",
    "P20_Cargando_y_gestionando_conductores.md"
]
INPUT_DIR = "test_docs"
OUTPUT_DIR = "test_docs/eval_results_v4"

def evaluate_translation(source_text, output_text, target_lang, gm):
    """Evalúa la precisión de la traducción verificando términos clave del glosario."""
    dnt = gm.glossary.get("app_context", {}).get("do_not_translate", [])
    
    # Excepción para pt-br
    if target_lang == "pt-br":
        dnt = [t for t in dnt if t not in ["Rostering", "Scheduling"]]
        
    found_dnt = [t for t in dnt if t in output_text]
    
    # Evaluar términos de negocio
    business_terms = gm.glossary.get("business_context", {}).get("es", {})
    expected_terms = []
    found_terms = []
    
    source_lower = source_text.lower()
    output_lower = output_text.lower()
    
    for src_term, translations in business_terms.items():
        if src_term.lower() in source_lower and target_lang in translations:
            exp = translations[target_lang].lower()
            expected_terms.append(exp)
            if exp in output_lower:
                found_terms.append(exp)
                
    # Evaluaciones exclusivas pt-br
    if target_lang == "pt-br":
        if "rostering" in source_lower: expected_terms.append("escalas")
        if "escalas" in output_lower: found_terms.append("escalas")
        
        if "scheduling" in source_lower: expected_terms.append("programação")
        if "programação" in output_lower or "programacao" in output_lower: found_terms.append("programação")
                
    return {
        "dnt_total": len(dnt),
        "dnt_found": len(found_dnt),
        "biz_total": len(expected_terms),
        "biz_found": len(found_terms)
    }

def run_evaluation():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    gm = GlossaryManager("glosario.json")
    
    report_lines = [
        "# 📊 Reporte de Evaluación de Modelos (GoalBus AI)",
        f"> **Fecha:** {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "Este reporte compara la precisión de diferentes modelos LLM basados en el glosario técnico y restricciones de traducción.",
        "\n---"
    ]
    
    for model_id in MODELS_TO_TEST:
        model_info = SUPPORTED_MODELS.get(model_id)
        if not model_info: continue
        
        print(f"\n[===== INICIANDO MODELO: {model_info['name']} =====]")
        report_lines.append(f"\n## 🤖 Modelo: {model_info['name']}")
        
        engine = AIEngine()
        try:
            print(f"Cargando {model_id} (esto puede descargar el modelo si no existe)...")
            engine.load_model(model_repo=model_info["repo_id"], model_filename=model_info["filename"])
            print("Carga exitosa.")
        except Exception as e:
            print(f"Error cargando {model_id}: {e}")
            report_lines.append(f"**Error de carga:** {e}")
            continue
            
        translator = MarkdownTranslator(engine, gm)
        
        for lang in LANGUAGES:
            print(f"\n  -> Idioma Objetivo: {lang.upper()}")
            lang_dir = os.path.join(OUTPUT_DIR, model_id, lang)
            os.makedirs(lang_dir, exist_ok=True)
            
            for file_name in FILES_TO_TEST:
                input_path = os.path.join(INPUT_DIR, file_name)
                if not os.path.exists(input_path):
                    print(f"     [!] Archivo no encontrado: {input_path}")
                    continue
                    
                print(f"     Traduciendo: {file_name} ...", end="", flush=True)
                start_time = time.time()
                
                try:
                    # Traducir nombre del archivo
                    translated_file_name = translator.translate_path(file_name, source_lang="es", target_lang=lang)
                    output_path = os.path.join(lang_dir, translated_file_name)
                    
                    translator.translate_file(input_path, output_path, source_lang="es", target_lang=lang)
                    elapsed = time.time() - start_time
                    
                    with open(input_path, "r", encoding="utf-8") as f:
                        source_text = f.read()
                    with open(output_path, "r", encoding="utf-8") as f:
                        output_text = f.read()
                        
                    eval_results = evaluate_translation(source_text, output_text, lang, gm)
                    
                    dnt_score = f"{eval_results['dnt_found']}/{eval_results['dnt_total']}"
                    biz_score = f"{eval_results['biz_found']}/{eval_results['biz_total']}"
                    
                    report_lines.append(f"### 📄 {file_name} -> `{translated_file_name}` (`{lang.upper()}`)")
                    report_lines.append(f"- **Tiempo:** {elapsed:.1f} segundos")
                    report_lines.append(f"- **DNT (No Traducir) Preservados:** {dnt_score}")
                    report_lines.append(f"- **Términos de Negocio Encontrados:** {biz_score}")
                    report_lines.append("\n")
                    
                    print(f" [OK] {elapsed:.1f}s | DNT: {dnt_score} | Biz: {biz_score} | Output Name: {translated_file_name}")
                    
                except Exception as e:
                    print(f" [ERROR] {e}")
                    report_lines.append(f"### 📄 {file_name} -> `{lang.upper()}`")
                    report_lines.append(f"- **Error durante traducción:** {e}\n")

    # Guardar reporte
    report_path = os.path.join(OUTPUT_DIR, "REPORTE_EVALUACION.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
        
    print(f"\n==============================================")
    print(f"✅ EVALUACIÓN FINALIZADA.")
    print(f"📂 Resultados y archivos en: {OUTPUT_DIR}")
    print(f"📊 Reporte de métricas en: {report_path}")

if __name__ == '__main__':
    run_evaluation()
