#!/bin/bash
cd "$(dirname "$0")"

echo "=== GoalBus Markdown Translator AI ==="
echo "Preparando entorno en Linux..."

if ! command -v python3 &> /dev/null
then
    echo "Python3 no está instalado. Por favor instala Python3 primero."
    exit 1
fi

if [ ! -d ".venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv .venv
fi

source .venv/bin/activate

echo "Instalando dependencias (si aplica)..."
pip install -q -r requirements.txt

echo "Iniciando servidor de IA..."
xdg-open "http://127.0.0.1:5050" || true

python app.py
