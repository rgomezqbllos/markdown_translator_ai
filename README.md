# 🌐 Markdown Translator AI - GoalBus

Una herramienta potente y local para la traducción masiva de archivos Markdown, diseñada específicamente para mantener la integridad técnica y la consistencia en documentaciones complejas.

## ✨ Características Principales

- **🤖 Modelos de IA Locales**: Soporta Llama 3.1, Gemma 2, Mistral, Phi-3 y Command R a través de GGUF (llama-cpp). Sin APIs externas (privacidad total).
- **📂 Traducción de Estructuras**: No solo traduce el contenido, sino también los nombres de archivos y carpetas, manteniendo la jerarquía del proyecto.
- **📖 Glosario Técnico**: Utiliza un motor de glosario inteligente (`glosario.json`) para asegurar que términos técnicos específicos no se traduzcan incorrectamente.
- **☁️ Soporte para Nube (iCloud)**: Detecta y fuerza la descarga de archivos gestionados por iCloud en macOS para evitar errores de archivo no encontrado.
- **⚡ Progreso en Tiempo Real**: Interfaz web moderna con logs detallados del proceso de traducción.
- **🚫 Control Total**: Botón de cancelación inmediata y manejo inteligente de errores.

## 🚀 Requisitos Previos

1. **Python 3.10+**: Asegúrate de tener Python instalado en tu sistema.
2. **Espacio en Disco**: Los modelos de IA se descargarán automáticamente la primera vez y requieren varios GB (Llama 3.1 ocupa ~5GB).
3. **RAM**: 
   - 8GB RAM: Recomendado para modelos como Llama 3 o Phi-3.
   - 16GB+ RAM: Requerido para modelos grandes como Command R.

## 🛠️ Cómo Iniciar el Proyecto

### Opción 1: Scripts Automáticos (Recomendado)

El proyecto incluye scripts que configuran el entorno virtual e instalan dependencias automáticamente:

- **macOS**: Haz doble clic en `start_mac.command` o ejecútalo desde la terminal:
  ```bash
  ./start_mac.command
  ```
- **Windows**: Ejecuta `start.bat`.
- **Linux**: Ejecuta `start_linux.sh`.

### Opción 2: Inicio Manual

Si prefieres hacerlo manualmente:

1. **Crear entorno virtual**:
   ```bash
   python -p venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```
2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configurar variables**:
   - Copia `.env.example` a `.env`.
   - (Opcional) Añade tu `HF_TOKEN` si deseas descargar modelos restringidos de HuggingFace.
4. **Ejecutar**:
   ```bash
   python app.py
   ```

Una vez iniciado, abre **[http://127.0.0.1:5050](http://127.0.0.1:5050)** en tu navegador.

## 📖 Cómo Usar

1. **Seleccionar Carpeta de Entrada**: Elige el directorio que contiene los archivos `.md` que deseas traducir.
2. **Seleccionar Carpeta de Salida**: Elige dónde quieres que se guarden los archivos traducidos (se recomienda una carpeta vacía).
3. **Elegir Idiomas**: Selecciona el idioma de origen y el de destino.
4. **Seleccionar Modelo**: 
   - *Llama 3.1 (8B)* es el balance ideal entre velocidad y calidad.
   - *Phi-3 Mini* es excelente para máquinas con menos recursos.
5. **Iniciar Traducción**: Haz clic en "Iniciar Traducción" y observa el progreso en el log.

## 📁 Estructura del Proyecto

- `app.py`: Servidor Flask y API.
- `core/`: Lógica interna (Motor AI, Traductor de Markdown, Gestor de Glosario).
- `models/`: Carpeta donde se descargan y guardan los modelos `.gguf`.
- `static/` & `templates/`: Interfaz de usuario web.
- `glosario.json`: Diccionario de términos técnicos para preservar.

---
*Desarrollado para la automatización de documentación técnica con IA Local.*

## 🛠️ Solución de Problemas (Windows)

Si encuentras errores al ejecutar el proyecto en Windows, consulta estas soluciones comunes:

### 1. Error `0xc000001d` o `ILLEGAL_INSTRUCTION`
Este error ocurre cuando tu procesador no soporta las instrucciones **AVX2** incluidas en las versiones pre-compiladas de `llama-cpp-python`.
**Solución:**
1. Instala [Visual Studio Build Tools](https://aka.ms/vs/17/release/vs_buildtools.exe) marcando la opción **"Desarrollo para el escritorio con C++"**.
2. Abre una terminal (PowerShell), activa el entorno y reinstala la librería sin AVX:
   ```powershell
   $env:CMAKE_ARGS="-DLLAMA_AVX=OFF -DLLAMA_AVX2=OFF -DLLAMA_FMA=OFF"
   pip install llama-cpp-python --force-reinstall --no-cache-dir
   ```

### 2. Error al instalar `llama-cpp-python` (Falta CMake/Compilador)
Si el script `start.bat` falla al instalar dependencias, es porque `pip` intenta compilar la librería y no encuentra un compilador.
**Solución:**
El archivo `start.bat` ha sido actualizado para usar el repositorio de paquetes pre-compilados de `abetlen`. Si el error persiste, asegúrate de tener instalado Python 3.10 o superior y vuelve a intentar.

### 3. El explorador de archivos no se abre
Se ha actualizado el motor de selección de carpetas en Windows para usar `tkinter`. Esto garantiza que la ventana de selección aparezca siempre en primer plano por encima del navegador. Si por alguna razón no aparece, revisa que no haya quedado minimizada en la barra de tareas.

