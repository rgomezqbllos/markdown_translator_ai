import os
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

class AIEngine:
    def __init__(self, models_dir: str = "models"):
        self.models_dir = os.path.abspath(models_dir)
        self.model_repo = None
        self.model_filename = None
        self.llm = None
        
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
        
        model_path = self._download_model_if_needed(model_repo, model_filename)
        print(f"Loading model {model_filename} into memory...")
        self.llm = Llama(
            model_path=model_path,
            n_ctx=4096,
            n_gpu_layers=-1, 
            verbose=False
        )
        print("Model loaded successfully.")

    def translate_text(self, text: str, system_prompt: str, target_lang: str) -> str:
        if not self.llm:
            raise Exception("Model not loaded. Call load_model() first.")
        
        response = self.llm.create_chat_completion(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Translate the following Markdown text to {target_lang}. Return ONLY the translated text, preserving all formatting:\n\n{text}"}
            ],
            max_tokens=2048,
            temperature=0.2, 
            stream=False
        )
        
        result = response['choices'][0]['message']['content'].strip()
        
        # Limpieza de "hallucinaciones" conversacionales clásicas de los LLMs
        lower_res = result.lower()
        if lower_res.startswith("here is the translated text") or lower_res.startswith("here's the translated text"):
            lines = result.split('\n', 1)
            if len(lines) > 1:
                result = lines[1].strip()
        
        return result
