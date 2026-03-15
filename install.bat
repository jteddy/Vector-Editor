@echo off
echo ================================
echo  Vector Editor — Setup
echo ================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [info] Python not found. Installing via winget...
    winget install -e --id Python.Python.3 --accept-source-agreements --accept-package-agreements
    if errorlevel 1 (
        echo [error] winget install failed.
        echo         Install manually from https://www.python.org/downloads/
        echo         Tick "Add Python to PATH" during install.
        pause
        exit /b 1
    )
    echo [ok] Python installed. Restarting setup...
    echo      You may need to open a new terminal for PATH to update.
    pause
    call "%~f0"
    exit /b
)

echo Installing dependencies...
pip install fastapi uvicorn

echo.
echo ================================
echo  Done. Run start.bat to launch.
echo ================================
pause
