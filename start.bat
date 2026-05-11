@echo off
title GoalBus Markdown Translator AI
cd /d "%~dp0"

echo === GoalBus Markdown Translator AI ===
echo Preparando entorno en Windows...

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python no esta instalado. Por favor instala Python3 primero.
    pause
    exit /b 1
)

IF NOT EXIST ".venv" (
    echo Creando entorno virtual...
    python -m venv .venv
)

call .venv\Scripts\activate.bat

echo Instalando dependencias (si aplica)...
pip install -q -r requirements.txt --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu --prefer-binary

echo Iniciando servidor de IA...
start http://127.0.0.1:5050

python app.py
pause
