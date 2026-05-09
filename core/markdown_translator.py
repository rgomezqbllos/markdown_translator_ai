import os
import re
from core.ai_engine import AIEngine
from core.glossary_manager import GlossaryManager

class MarkdownTranslator:
    def __init__(self, engine: AIEngine, glossary_manager: GlossaryManager):
        self.engine = engine
        self.glossary_manager = glossary_manager

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

    def chunk_markdown(self, content: str, max_chars: int = 1500) -> list:
        chunks = []
        
        # 1. Aislar YAML Frontmatter
        if content.startswith('---'):
            parts = content.split('\n---\n', 1)
            if len(parts) > 1:
                chunks.append(parts[0] + '\n---')
                content = parts[1]
                
        # 2. Agrupar bloques hasta max_chars
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

    def translate_document(self, content: str, source_lang: str, target_lang: str, cancel_callback=None) -> str:
        base_prompt = self.glossary_manager.get_system_prompt(source_lang, target_lang)
        sys_prompt = (
            f"{base_prompt}\n\n"
            "RULES FOR MARKDOWN TRANSLATION:\n"
            f"1. You are a professional software translator. You MUST translate ALL human-readable text into {target_lang}.\n"
            "2. DO NOT copy the original text unless it is a proper noun (like GoalBus).\n"
            "3. PRESERVE ALL Markdown syntax exactly (like # headers, * italics, ** bold, `code`, ```code blocks```, [links](url), ![images](url), and YAML ---).\n"
            "4. PRESERVE ALL HTML tags exactly as they are (e.g. <div id=\"G_REF_...\"></div>).\n"
            "5. Do NOT translate URLs, code syntax, or technical file paths.\n"
            "6. OUTPUT ONLY THE TRANSLATED TEXT. No conversational intros."
        )
        
        # Ocultar las referencias de imágenes ANTES del chunking para mantener bloques grandes de contexto
        safe_content, placeholders = self.hide_special_blocks(content)
        chunks = self.chunk_markdown(safe_content)
        translated_chunks = []
        
        for i, chunk in enumerate(chunks):
            if cancel_callback and cancel_callback():
                break
                
            if not chunk.strip():
                continue
            
            # Si el chunk es puramente frontmatter, podemos pasarlo directamente o traducirlo
            # En este caso, lo pasamos por la IA porque tiene title e intro
            print(f"    -> Traduciendo fragmento {i+1}/{len(chunks)} ({len(chunk)} caracteres)...")
            translated_text = self.engine.translate_text(chunk, sys_prompt, target_lang)
            translated_chunks.append(translated_text)
            
        final_text = '\n\n'.join(translated_chunks)
        # Restaurar las referencias originales
        final_text = self.restore_special_blocks(final_text, placeholders)
        
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
        
        sys_prompt = (
            f"You are a translator. Translate this file or folder name from {source_lang} to {target_lang}. "
            "Output ONLY the translated name. Do NOT include file extensions in the output if they weren't in the input. "
            "Preserve formatting like underscores (_) or hyphens (-) or numbers."
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
                    translated_base = self.engine.translate_text(base_name, sys_prompt, target_lang).strip()
                    translated_base = translated_base.replace('"', '').replace("'", "")
                    
                    if translated_base:
                        translated_name = prefix + translated_base
                        translated_parts.append(translated_name + ext)
                    else:
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
