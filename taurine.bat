@echo off
setlocal
echo ============================================
echo === Avvio script anti-standby [%date% %time%]
echo ============================================

REM 1. Controllo che Python sia disponibile
where python >nul 2>&1
if errorlevel 1 (
    echo [ERRORE] Python non trovato nel PATH.
    exit /b 1
)

REM 2. Crea .venv se non esiste
if not exist .venv (
    echo [INFO] Creazione ambiente virtuale...
    python -m venv .venv
    if errorlevel 1 (
        echo [ERRORE] Creazione virtualenv fallita.
        exit /b 1
    )
)

REM 3. Attiva ambiente virtuale
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERRORE] Attivazione virtualenv fallita.
    exit /b 1
)

REM 4. Installa librerie da requirements.txt
if not exist requirements.txt (
    echo [ERRORE] File requirements.txt non trovato.
    exit /b 1
)

echo [INFO] Installazione dipendenze...
pip install -r requirements.txt

REM 5. Esecuzione script Python
echo [INFO] Esecuzione script taurine.py...
python taurine.py

REM 6. Fine
echo ============================================
echo === Fine esecuzione [%date% %time%]
echo ============================================
endlocal
