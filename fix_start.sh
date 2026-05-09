#!/bin/bash
cd "$(dirname "$0")"

echo "=== GoalBus Markdown Translator AI ==="
echo "Preparando entorno en Mac (Versión Corregida)..."

# Find a working python3
WORKING_PYTHON=""
for py in "/Library/Frameworks/Python.framework/Versions/3.12/bin/python3" "/opt/homebrew/bin/python3" "/usr/local/bin/python3" "/usr/bin/python3" "python3"; do
    if command -v "$py" &> /dev/null; then
        if "$py" -c "import sys; print('ok')" &> /dev/null; then
            WORKING_PYTHON="$py"
            break
        fi
    fi
done

if [ -z "$WORKING_PYTHON" ]; then
    echo "No se encontró una versión de Python3 funcional. Por favor instala Python3."
    exit 1
fi

echo "Usando Python: $WORKING_PYTHON"

# Limpiar venv roto si existe
if [ -d ".venv" ]; then
    if ! .venv/bin/python3 -c "import sys" &> /dev/null; then
        echo "Entorno virtual roto detectado. Recreando..."
        rm -rf .venv
    fi
fi

if [ ! -d ".venv" ]; then
    echo "Creando entorno virtual..."
    "$WORKING_PYTHON" -m venv .venv
fi

source .venv/bin/activate

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Iniciando servidor de IA..."
# Abre el navegador en mac
open "http://127.0.0.1:5050"

python app.py
