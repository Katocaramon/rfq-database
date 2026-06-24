@echo off
chcp 65001 > nul
title RFQ Database

echo.
echo  ============================================================
echo   RFQ Database - Avvio server
echo  ============================================================
echo.

REM --- Verifica che il file .env esista ---
if not exist ".env" (
    echo  [ERRORE] File .env non trovato!
    echo  Copia .env.example in .env e compila i valori.
    echo.
    pause
    exit /b 1
)

REM --- Attiva virtual environment se presente ---
if exist ".venv\Scripts\activate.bat" (
    echo  Attivazione virtual environment...
    call .venv\Scripts\activate.bat
) else if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

REM --- Avvia il server ---
echo  Avvio in corso... (premi Ctrl+C per fermare)
echo.
python run.py

echo.
echo  Server arrestato.
pause
