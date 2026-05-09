import sys
from core.glossary_manager import GlossaryManager
from core.ai_engine import AIEngine

def main():
    print("--- Probando Traductor GoalBus (Fase 1) ---")
    
    source_lang = "es"
    target_lang = "en"
    
    # 1. Cargar el glosario y generar el prompt
    gm = GlossaryManager("glosario.json")
    sys_prompt = gm.get_system_prompt(source_lang, target_lang)
    
    print("\n--- System Prompt Generado ---")
    print(sys_prompt)
    print("------------------------------\n")
    
    # 2. Inicializar el motor de IA
    engine = AIEngine()
    
    # IMPORTANTE: La primera vez descargará ~2.3GB. 
    # Para probar sin esperar la descarga, puedes comentar la carga del modelo 
    # y simular la respuesta.
    
    print("Iniciando carga del modelo (esto puede tardar si necesita descargar)...")
    try:
        engine.load_model()
    except Exception as e:
        print(f"Error cargando el modelo: {e}")
        print("Asegúrate de haber ejecutado: pip install -r requirements.txt")
        sys.exit(1)
        
    # 3. Prueba de traducción
    texto_prueba = "El módulo de Planning genera el cuadrante de trabajo para cada expedición."
    print(f"\nTexto Original ({source_lang}): {texto_prueba}")
    print("Traduciendo...")
    
    resultado = engine.translate_text(texto_prueba, sys_prompt)
    
    print(f"\nTraducción ({target_lang}): {resultado}")

if __name__ == "__main__":
    main()
