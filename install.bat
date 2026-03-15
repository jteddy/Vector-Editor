@echo off
echo ================================
echo  Recoil Editor — Setup
echo ================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [error] Python not found.
    echo         Download from https://www.python.org/downloads/
    echo         Tick "Add Python to PATH" during install.
    pause
    exit /b 1
)

echo Installing dependencies...
pip install fastapi uvicorn

echo.
echo ================================
echo  Done. Run start.bat to launch.
echo ================================
pause
