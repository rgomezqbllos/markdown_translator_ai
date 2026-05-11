import os
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

class AIEngine:
    def __init__(self, models_dir: str = "models"):
        self.models_dir = os.path.abspath(models_dir)
        self.model_repo = None
        self.model_filename = None
        self.llm = None
        self._supports_system_role = True  # Se auto-detecta en la primera llamada
        
    def _download_model_if_needed(self, model_repo: str, model_filename: str) -> str:
        if not os.path.exists(self.models_dir):
            os.makedirs(self.models_dir)
            
        local_path = os.path.join(self.models_dir, model_filename)
        if not os.path.exists(local_path):
            print(f"Downloading {model_filename} from {model_repo}...")
            downloaded_path = hf_hub_download(
                repo_id=model_repo, 
                filename=model_filename, 
                local_dir=self.models_dir,
                local_dir_use_symlinks=False,
                token=os.environ.get("HF_TOKEN")
            )
            print("Download complete.")
            return downloaded_path
        
        return local_path

    def load_model(self, model_repo: str = "microsoft/Phi-3-mini-4k-instruct-gguf", model_filename: str = "Phi-3-mini-4k-instruct-q4.gguf"):
        if self.llm and self.model_repo == model_repo and self.model_filename == model_filename:
            return # Ya está cargado
            
        if self.llm:
            print("Unloading previous model...")
            del self.llm
            self.llm = None
            
        self.model_repo = model_repo
        self.model_filename = model_filename
        self._supports_system_role = True  # Reset al cargar un nuevo modelo
        
        model_path = self._download_model_if_needed(model_repo, model_filename)
        print(f"Loading model {model_filename} into memory...")
        self.llm = Llama(
            model_path=model_path,
            n_ctx=4096,
            n_gpu_layers=-1, 
            verbose=False
        )
        print("Model loaded successfully.")

    def _build_messages(self, system_prompt: str, user_content: str) -> list:
        """Construye los mensajes según la capacidad del modelo."""
        if self._supports_system_role:
            return [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ]
        else:
            # Fusionar system prompt en el mensaje del usuario
            merged = f"{system_prompt}\n\n{user_content}"
            return [{"role": "user", "content": merged}]

    def translate_text(self, text: str, system_prompt: str, target_lang: str, max_tokens: int = 2048) -> str:
        """Traduce texto usando el LLM cargado.
        
        Args:
            text: Texto a traducir
            system_prompt: Instrucciones del sistema
            target_lang: Idioma destino
            max_tokens: Límite de tokens en la respuesta (default 2048, usar menos para campos cortos)
        """
        if not self.llm:
            raise Exception("Model not loaded. Call load_model() first.")
        
        user_content = f"Translate the following text to {target_lang}. Return ONLY the translated text, nothing else:\n\n{text}"
        messages = self._build_messages(system_prompt, user_content)
        
        try:
            response = self.llm.create_chat_completion(
                messages=messages,
                max_tokens=max_tokens,
                temperature=0.1,  # Más bajo = más determinista, menos alucinación
                top_p=0.9,
                repeat_penalty=1.2,  # Penaliza repetición para evitar loops
                stream=False
            )
        except ValueError as e:
            if "System role not supported" in str(e):
                # Marcar que este modelo NO soporta system role y reintentar
                self._supports_system_role = False
                print("    [INFO] Modelo sin soporte de system role, usando modo fusionado.")
                messages = self._build_messages(system_prompt, user_content)
                response = self.llm.create_chat_completion(
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=0.1,
                    top_p=0.9,
                    repeat_penalty=1.2,
                    stream=False
                )
            else:
                raise e
        
        result = response['choices'][0]['message']['content'].strip()
        
        # Limpieza de "hallucinaciones" conversacionales clásicas de los LLMs
        lower_res = result.lower()
        for prefix in ["here is the translated text", "here's the translated text", 
                        "translation:", "translated text:", "here is the translation"]:
            if lower_res.startswith(prefix):
                lines = result.split('\n', 1)
                if len(lines) > 1:
                    result = lines[1].strip()
                break
        
        return result
