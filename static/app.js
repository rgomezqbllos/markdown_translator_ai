document.addEventListener('DOMContentLoaded', () => {
    const sourceLangSelect = document.getElementById('source_lang');
    const targetLangSelect = document.getElementById('target_lang');
    const modelSelect = document.getElementById('model_select');
    const translateBtn = document.getElementById('translate_btn');
    const consoleOutput = document.getElementById('console_output');
    const btnText = document.querySelector('.btn-text');
    
    // Nombres de idiomas legibles
    const langNames = {
        'es': 'Español',
        'en': 'Inglés',
        'pt-br': 'Portugués (Brasil)',
        'pt-pt': 'Portugués (Portugal)',
        'fr': 'Francés',
        'de': 'Alemán',
        'it': 'Italiano',
        'ar': 'Árabe'
    };

    // 1. Cargar idiomas disponibles
    fetch('/api/languages')
        .then(res => res.json())
        .then(langs => {
            langs.forEach(lang => {
                const name = langNames[lang] || lang.toUpperCase();
                const option1 = new Option(name, lang);
                const option2 = new Option(name, lang);
                sourceLangSelect.add(option1);
                targetLangSelect.add(option2);
            });
            // Defaults
            sourceLangSelect.value = 'es';
            targetLangSelect.value = 'en';
        })
        .catch(err => logToConsole('Error cargando idiomas: ' + err, 'error'));

    // 1.5 Cargar modelos disponibles
    fetch('/api/models')
        .then(res => res.json())
        .then(models => {
            for (const [id, info] of Object.entries(models)) {
                const option = new Option(info.name, id);
                modelSelect.add(option);
            }
            if (models['llama3_8b']) {
                modelSelect.value = 'llama3_8b';
            }
        })
        .catch(err => logToConsole('Error cargando modelos: ' + err, 'error'));

    // Utilidad para logs
    function logToConsole(message, type = 'info') {
        const div = document.createElement('div');
        div.className = `log-line ${type}`;
        div.textContent = message;
        consoleOutput.appendChild(div);
        consoleOutput.scrollTop = consoleOutput.scrollHeight;
    }

    // 2. Manejar selección de carpetas nativa
    document.querySelectorAll('.browse-btn').forEach(btn => {
        btn.addEventListener('click', async () => {
            const targetId = btn.getAttribute('data-target');
            const targetInput = document.getElementById(targetId);
            const originalText = btn.textContent;
            
            btn.textContent = '...';
            btn.disabled = true;
            
            try {
                const res = await fetch('/api/browse_folder', { method: 'POST' });
                const data = await res.json();
                
                if (data.folder) {
                    targetInput.value = data.folder;
                } else if (data.error) {
                    alert('Error abriendo el explorador: ' + data.error);
                }
            } catch (err) {
                console.error(err);
                alert('No se pudo abrir el explorador de archivos.');
            }
            
            btn.textContent = originalText;
            btn.disabled = false;
        });
    });

    const stopBtn = document.getElementById('stop_btn');
    
    // ...

    // 4. Manejar cancelación
    stopBtn.addEventListener('click', async () => {
        stopBtn.disabled = true;
        stopBtn.querySelector('.btn-text').textContent = 'Deteniendo...';
        
        try {
            await fetch('/api/stop', { method: 'POST' });
        } catch(e) {
            console.error('Error al detener', e);
        }
    });

    // 3. Manejar la traducción masiva
    translateBtn.addEventListener('click', async () => {
        const input_dir = document.getElementById('input_dir').value;
        const output_dir = document.getElementById('output_dir').value;
        const source_lang = sourceLangSelect.value;
        const target_lang = targetLangSelect.value;
        const model_id = modelSelect.value;

        if (!input_dir || !output_dir) {
            alert('Por favor selecciona los directorios de entrada y salida con los botones "Explorar".');
            return;
        }

        consoleOutput.innerHTML = '';
        translateBtn.style.display = 'none';
        stopBtn.style.display = 'block';
        stopBtn.disabled = false;
        stopBtn.querySelector('.btn-text').textContent = 'Detener';
        
        try {
            const response = await fetch('/api/translate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ input_dir, output_dir, source_lang, target_lang, model_id })
            });

            if (!response.ok) {
                const err = await response.json();
                logToConsole(`Error: ${err.error}`, 'error');
                translateBtn.style.display = 'flex';
                stopBtn.style.display = 'none';
                return;
            }

            // Streaming logs
            const reader = response.body.getReader();
            const decoder = new TextDecoder('utf-8');

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;
                
                const chunk = decoder.decode(value, { stream: true });
                const lines = chunk.split('\n\n');
                
                for (let line of lines) {
                    if (line.startsWith('data: ')) {
                        const msg = line.substring(6).trim();
                        if (!msg) continue;
                        
                        if (msg === 'TRADUCCION_FINALIZADA' || msg.includes('CANCELADA')) {
                            if (msg === 'TRADUCCION_FINALIZADA') {
                                logToConsole('¡Traducción completada con éxito!', 'success');
                            } else {
                                logToConsole('Traducción cancelada.', 'warn');
                            }
                            translateBtn.style.display = 'flex';
                            stopBtn.style.display = 'none';
                        } else if (msg.includes('[ERROR]')) {
                            logToConsole(msg, 'error');
                        } else if (msg.includes('[OK]')) {
                            logToConsole(msg, 'success');
                        } else if (msg.includes('[WARN]')) {
                            logToConsole(msg, 'warn');
                        } else {
                            logToConsole(msg, 'info');
                        }
                    }
                }
            }
        } catch (error) {
            logToConsole(`Falló la conexión: ${error.message}`, 'error');
            translateBtn.style.display = 'flex';
            stopBtn.style.display = 'none';
        }
    });
});
