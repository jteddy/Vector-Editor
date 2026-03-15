@echo off
cd /d "%~dp0"

echo ================================
echo  Recoil Editor
echo ================================
echo.

:: Check dependencies
python -c "import fastapi, uvicorn" >nul 2>&1
if errorlevel 1 (
    echo [error] Missing dependencies. Run install.bat first.
    pause
    exit /b 1
)

:: Use Python to kill anything on port 8000
python -c "import subprocess,sys; r=subprocess.run('netstat -aon',capture_output=True,text=True); lines=[l for l in r.stdout.splitlines() if ':8000 ' in l and 'LISTENING' in l]; [subprocess.run(f'taskkill /PID {l.split()[-1]} /F',shell=True) for l in lines]; print('Cleared port 8000.' if lines else 'Port 8000 is free.')"

echo.
echo Starting server...
echo Open http://localhost:8000 in your browser
echo Press Ctrl+C to stop.
echo.

python "%~dp0app.py"
pause
