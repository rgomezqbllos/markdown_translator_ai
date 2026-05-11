import json
import os

class GlossaryManager:
    def __init__(self, glossary_path: str = "glosario.json"):
        self.glossary_path = glossary_path
        self.glossary = self._load_glossary()

    def _load_glossary(self) -> dict:
        if not os.path.exists(self.glossary_path):
            return {"app_context": {"do_not_translate": []}, "business_context": {}, "language_instructions": {}}
        with open(self.glossary_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_system_prompt(self, source_lang: str, target_lang: str) -> str:
        """
        Construye el system prompt combinando las instrucciones del idioma, 
        el contexto de la aplicación y el diccionario de negocio.
        """
        # Instrucción base
        base_instruction = self.glossary.get("language_instructions", {}).get(
            target_lang,
            f"You are an expert translator. Translate the following text from {source_lang} to {target_lang}."
        )

        # Contexto de la aplicación
        do_not_translate = self.glossary.get("app_context", {}).get("do_not_translate", [])
        
        # Excepción específica para pt-br
        if target_lang == "pt-br":
            do_not_translate = [term for term in do_not_translate if term not in ["Rostering", "Scheduling"]]

        if do_not_translate:
            dnt_str = ", ".join(do_not_translate)
            app_context = f"\nDO NOT translate these software terms: {dnt_str}."
        else:
            app_context = ""

        # Contexto de negocio
        business_terms = []
        source_dict = self.glossary.get("business_context", {}).get(source_lang, {})
        for term, translations in source_dict.items():
            if target_lang in translations:
                business_terms.append(f"'{term}' -> '{translations[target_lang]}'")
        
        if business_terms:
            bus_str = "\n".join(business_terms)
            business_context = f"\nUse the following exact translations for business terms:\n{bus_str}"
        else:
            business_context = ""

        return f"{base_instruction}{app_context}{business_context}"
