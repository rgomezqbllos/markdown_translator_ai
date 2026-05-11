import os
import re
import yaml
from core.ai_engine import AIEngine
from core.glossary_manager import GlossaryManager

class MarkdownTranslator:
    def __init__(self, engine: AIEngine, glossary_manager: GlossaryManager):
        self.engine = engine
        self.glossary_manager = glossary_manager

    # Mapa de códigos de idioma a nombres completos para claridad en prompts
    LANG_NAMES = {
        "en": "English", "pt-br": "Brazilian Portuguese", "pt-pt": "European Portuguese",
        "fr": "French", "de": "German", "it": "Italian", "ar": "Arabic",
        "es": "Spanish", "zh": "Chinese", "ja": "Japanese", "ko": "Korean"
    }

    def hide_special_blocks(self, content: str) -> tuple:
        """Oculta bloques ref: usando etiquetas HTML estándar que la IA respeta 100%."""
        placeholders = {}
        counter = 0
        lines = content.split('\n')
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('ref:') or stripped.startswith('`ref:'):
                ph_tag = f'<div id="G_REF_{counter}"></div>'
                placeholders[ph_tag] = line
                lines[i] = ph_tag
                counter += 1
        return '\n'.join(lines), placeholders

    def restore_special_blocks(self, content: str, placeholders: dict) -> str:
        """Devuelve las líneas ref: originales al texto traducido."""
        for ph_tag, original in placeholders.items():
            # Expresión regular por si la IA añade espacios por accidente
            ph_pattern = r'<div id="' + re.escape(re.search(r'id="([^"]+)"', ph_tag).group(1)) + r'">\s*</div>'
            content = re.sub(ph_pattern, original, content)
        return content

    def extract_frontmatter(self, content: str) -> tuple:
        """Extrae el YAML frontmatter del contenido para protegerlo.
        Retorna (frontmatter_dict, body) o (None, content) si no hay frontmatter."""
        if not content.startswith('---'):
            return None, content
        
        # Buscar el cierre del frontmatter
        end_match = re.search(r'\n---\s*\n', content[3:])
        if not end_match:
            return None, content
        
        fm_end = end_match.end() + 3  # +3 por los primeros '---'
        fm_raw = content[4:end_match.start() + 3]  # Contenido entre los ---
        body = content[fm_end:]
        
        try:
            fm_dict = yaml.safe_load(fm_raw)
            if not isinstance(fm_dict, dict):
                return None, content
            return fm_dict, body
        except yaml.YAMLError:
            return None, content

    def _translate_short_text(self, text: str, target_lang: str, field_name: str) -> str:
        """Traduce un texto corto (título, shortTitle, intro) con protección anti-alucinación.
        
        Usa max_tokens limitado y valida que la salida no sea absurdamente larga.
        """
        lang_name = self.LANG_NAMES.get(target_lang, target_lang)
        
        # Prompt ultra-específico para campos cortos
        sys_prompt = (
            f"You are a translator. Translate the text to {lang_name}.\n"
            f"RULES:\n"
            f"- Output ONLY the translation, nothing else.\n"
            f"- Do NOT add explanations, headers (#), markdown formatting, or extra content.\n"
            f"- Do NOT invent or elaborate. The translation must have similar length to the original.\n"
            f"- The output language MUST be {lang_name}.\n"
            f"- Keep proper nouns like GoalBus, GoalDriver, Planning, Scheduling, Rostering, Dispatching, Bidding unchanged."
        )
        
        # Calcular max_tokens proporcional al input (pero mínimo 50, máximo 200)
        # Estimación: 1 token ≈ 4 chars, multiplicamos x3 para dar margen multilingüe
        estimated_tokens = max(50, min(200, (len(text) // 4) * 3))
        
        result = self.engine.translate_text(text, sys_prompt, target_lang, max_tokens=estimated_tokens)
        
        # Validación: si el resultado es >4x más largo que el input, algo salió mal
        if len(result) > len(text) * 4:
            print(f"    [WARN] Frontmatter.{field_name} alucinó ({len(result)} chars vs {len(text)} original). Usando original.")
            return text
        
        # Limpiar caracteres de markdown que los modelos insertan por error
        result = result.lstrip('#').strip()
        result = result.strip("'\"")
        
        return result

    def translate_frontmatter(self, fm_dict: dict, target_lang: str) -> dict:
        """Traduce solo los valores textuales del frontmatter con protección anti-alucinación."""
        translatable_keys = ['title', 'shortTitle', 'intro']
        translated = dict(fm_dict)
        
        for key in translatable_keys:
            if key in translated and isinstance(translated[key], str):
                print(f"    -> Traduciendo frontmatter.{key}...")
                translated[key] = self._translate_short_text(
                    translated[key], target_lang, key
                )
        
        return translated

    def rebuild_frontmatter(self, fm_dict: dict) -> str:
        """Reconstruye el bloque YAML frontmatter desde el diccionario."""
        lines = ['---']
        for key, value in fm_dict.items():
            if isinstance(value, str):
                # Escapar comillas simples dentro del valor
                escaped = value.replace("'", "''")
                # Usar comillas simples siempre para seguridad
                lines.append(f"{key}: '{escaped}'")
            elif isinstance(value, list):
                lines.append(f"{key}:")
                for item in value:
                    if isinstance(item, str):
                        lines.append(f"  - '{item}'")
                    else:
                        lines.append(f"  - {item}")
            else:
                lines.append(f"{key}: {value}")
        lines.append('---')
        return '\n'.join(lines)

    def chunk_markdown(self, content: str, max_chars: int = 1500) -> list:
        chunks = []
        
        # El frontmatter ya fue extraído antes, solo agrupar bloques
        blocks = content.split('\n\n')
        current_chunk = []
        current_length = 0
        in_code_block = False

        for block in blocks:
            if block.count('```') % 2 != 0:
                in_code_block = not in_code_block
                
            current_chunk.append(block)
            current_length += len(block)
            
            if current_length >= max_chars and not in_code_block:
                chunks.append('\n\n'.join(current_chunk))
                current_chunk = []
                current_length = 0
                
        if current_chunk:
            chunks.append('\n\n'.join(current_chunk))
            
        return chunks

    def enforce_dnt(self, text: str, target_lang: str) -> str:
        """Post-procesado: restaura términos DNT que el modelo haya traducido por error."""
        dnt_terms = self.glossary_manager.glossary.get("app_context", {}).get("do_not_translate", [])
        
        # Excepción PT-BR: Rostering y Scheduling sí se traducen
        if target_lang == "pt-br":
            dnt_terms = [t for t in dnt_terms if t not in ["Rostering", "Scheduling"]]
        
        # Mapeo de traducciones comunes incorrectas -> término original
        common_mistakes = {
            "Planificación": "Planning", "Planejamento": "Planning", "Planung": "Planning",
            "Pianificazione": "Planning", "Planification": "Planning", "التخطيط": "Planning",
            "Despacho": "Dispatching", "Versand": "Dispatching", "Expédition": "Dispatching",
            "Dispacciamento": "Dispatching", "Spedizione": "Dispatching",
            "Programación": "Scheduling", "Zeitplanung": "Scheduling",
            "Programmation": "Scheduling", "Programmazione": "Scheduling",
            "Licitación": "Bidding", "Licitação": "Bidding", "Bieten": "Bidding",
            "Offerta": "Bidding", "Enchères": "Bidding",
        }
        
        for wrong, correct in common_mistakes.items():
            if correct in dnt_terms:
                # Solo reemplazar como palabra completa, evitar falsos positivos
                text = re.sub(r'\b' + re.escape(wrong) + r'\b', correct, text)
        
        # Limpiar caracteres CJK que Qwen puede insertar por error en idiomas no-CJK
        if target_lang not in ['zh', 'ja', 'ko']:
            text = re.sub(r'[\u4e00-\u9fff\u3400-\u4dbf\u3000-\u303f]+', '', text)
        
        # Limpiar líneas que quedaron vacías tras eliminar CJK
        text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
        
        return text

    def translate_document(self, content: str, source_lang: str, target_lang: str, cancel_callback=None) -> str:
        base_prompt = self.glossary_manager.get_system_prompt(source_lang, target_lang)
        lang_name = self.LANG_NAMES.get(target_lang, target_lang)
        
        # Construir lista DNT explícita para el prompt
        dnt_terms = self.glossary_manager.glossary.get("app_context", {}).get("do_not_translate", [])
        if target_lang == "pt-br":
            dnt_display = [t for t in dnt_terms if t not in ["Rostering", "Scheduling"]]
        else:
            dnt_display = dnt_terms
        dnt_list = ', '.join(dnt_display)
        
        sys_prompt = (
            f"{base_prompt}\n\n"
            "RULES FOR MARKDOWN TRANSLATION:\n"
            f"1. You are a professional translator. You MUST translate ALL text into {lang_name}. "
            f"Every word of your output MUST be in {lang_name}. Do NOT leave any text in Spanish, Portuguese, English, or any other language.\n"
            f"2. Do NOT copy the original text. Translate everything.\n"
            "3. PRESERVE ALL Markdown syntax exactly (# headers, **bold**, *italics*, `code`, ```code blocks```, [links](url), ![images](url)).\n"
            "4. PRESERVE ALL HTML tags exactly as they are (e.g. <div id=\"G_REF_...\"></div>).\n"
            "5. Do NOT translate URLs, code syntax, or technical file paths.\n"
            "6. OUTPUT ONLY THE TRANSLATED TEXT. No introductions, no explanations, no comments.\n"
            f"7. CRITICAL: Keep these words EXACTLY as written, never translate them: {dnt_list}\n"
            "8. Preserve 'fileciteturn...' references exactly as they appear.\n"
            "9. Do NOT invent content. Translate only what is given."
        )
        
        # 1. Ocultar referencias de imágenes
        safe_content, placeholders = self.hide_special_blocks(content)
        
        # 2. Extraer y proteger el frontmatter YAML
        fm_dict, body = self.extract_frontmatter(safe_content)
        
        # 3. Traducir frontmatter de forma controlada (con límite de tokens)
        translated_fm = ""
        if fm_dict:
            translated_fm_dict = self.translate_frontmatter(fm_dict, target_lang)
            translated_fm = self.rebuild_frontmatter(translated_fm_dict)
        
        # 4. Dividir y traducir el body
        chunks = self.chunk_markdown(body)
        translated_chunks = []
        
        for i, chunk in enumerate(chunks):
            if cancel_callback and cancel_callback():
                break
                
            if not chunk.strip():
                continue
            
            print(f"    -> Traduciendo fragmento {i+1}/{len(chunks)} ({len(chunk)} caracteres)...")
            translated_text = self.engine.translate_text(chunk, sys_prompt, target_lang)
            
            # Validación: si un chunk crece más de 5x, probablemente alucinó
            if len(translated_text) > len(chunk) * 5:
                print(f"    [WARN] Fragmento {i+1} alucinó ({len(translated_text)} vs {len(chunk)} chars). Reintentando...")
                # Reintentar con temperatura 0
                translated_text = self.engine.translate_text(chunk, sys_prompt, target_lang, max_tokens=1024)
                if len(translated_text) > len(chunk) * 5:
                    print(f"    [WARN] Segundo intento también falló. Usando original.")
                    translated_text = chunk
            
            translated_chunks.append(translated_text)
        
        # 5. Ensamblar resultado
        body_text = '\n\n'.join(translated_chunks)
        
        if translated_fm:
            final_text = translated_fm + '\n\n' + body_text
        else:
            final_text = body_text
        
        # 6. Restaurar referencias originales
        final_text = self.restore_special_blocks(final_text, placeholders)
        
        # 7. Post-procesado: restaurar DNT y limpiar artefactos
        final_text = self.enforce_dnt(final_text, target_lang)
        
        return final_text

    def translate_file(self, input_path: str, output_path: str, source_lang: str, target_lang: str, cancel_callback=None):
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        translated_content = self.translate_document(content, source_lang, target_lang, cancel_callback)
        
        if cancel_callback and cancel_callback():
            return # No guardar archivo si se canceló a medias
            
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)

    def translate_path(self, rel_path: str, source_lang: str, target_lang: str) -> str:
        parts = rel_path.split(os.sep)
        translated_parts = []
        
        lang_name = self.LANG_NAMES.get(target_lang, target_lang)
        source_name = self.LANG_NAMES.get(source_lang, source_lang)
        
        sys_prompt = (
            f"You are a file name translator. Your output language MUST be {lang_name}.\n"
            f"Translate this file/folder name from {source_name} to {lang_name}.\n"
            f"CRITICAL RULES:\n"
            f"- Output MUST be in {lang_name}. Do NOT output in Spanish, Portuguese, Hebrew, Chinese, or any other language.\n"
            f"- Output ONLY the translated name, nothing else.\n"
            f"- Do NOT include file extensions (.md, .txt, etc).\n"
            f"- Preserve underscores (_) between words.\n"
            f"- Do NOT add explanations or quotes."
        )
        
        # Detecta prefijos como "01_", "P15_", "O9_", "R1.1_"
        prefix_pattern = re.compile(r'^([A-Za-z]{0,2}\d+(?:\.\d+)*_)')
        
        for part in parts:
            name, ext = os.path.splitext(part)
            if name.strip():
                # Proteger el prefijo alfanumérico
                prefix_match = prefix_pattern.match(name)
                if prefix_match:
                    prefix = prefix_match.group(1)
                    base_name = name[len(prefix):]
                else:
                    prefix = ""
                    base_name = name
                    
                if base_name.strip():
                    print(f"    -> Traduciendo ruta: {base_name}")
                    try:
                        # Limitar tokens para nombres de archivo (evitar alucinación)
                        max_tok = max(30, min(100, (len(base_name) // 4) * 3))
                        translated_base = self.engine.translate_text(
                            base_name, sys_prompt, target_lang, max_tokens=max_tok
                        ).strip()
                        translated_base = translated_base.replace('"', '').replace("'", "")
                        # Limpiar posibles extensiones que el modelo añade por error
                        if translated_base.endswith('.md'):
                            translated_base = translated_base[:-3]
                        # Reemplazar espacios por guiones bajos
                        translated_base = translated_base.replace(' ', '_')
                        # Eliminar caracteres problemáticos para sistemas de archivos
                        translated_base = re.sub(r'[<>:"|?*]', '', translated_base)
                        # Eliminar # que los modelos insertan por error
                        translated_base = translated_base.lstrip('#').strip('_').strip()
                        
                        # Validación: si el resultado es >4x el original, falló
                        if len(translated_base) > len(base_name) * 4:
                            print(f"    [WARN] Nombre alucinado. Usando original.")
                            translated_parts.append(part)
                            continue
                        
                        if translated_base:
                            translated_name = prefix + translated_base
                            print(f"    -> Ruta traducida: {translated_name}{ext}")
                            translated_parts.append(translated_name + ext)
                        else:
                            translated_parts.append(part)
                    except Exception as e:
                        print(f"    [WARN] No se pudo traducir la ruta, usando original: {e}")
                        translated_parts.append(part)
                else:
                    translated_parts.append(part)
            else:
                translated_parts.append(part)
                
        return os.path.join(*translated_parts)

    def translate_directory(self, input_dir: str, output_dir: str, source_lang: str, target_lang: str):
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith('.md'):
                    input_path = os.path.join(root, file)
                    rel_path = os.path.relpath(input_path, input_dir)
                    output_path = os.path.join(output_dir, rel_path)
                    
                    self.translate_file(input_path, output_path, source_lang, target_lang)
