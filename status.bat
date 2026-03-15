@echo off
cd /d "%~dp0"
echo Checking Vector Editor status...
echo.
python -c "import subprocess; r=subprocess.run('netstat -aon',capture_output=True,text=True); lines=[l for l in r.stdout.splitlines() if ':8000 ' in l and 'LISTENING' in l]; print('[RUNNING]  http://localhost:8000  (PID ' + lines[0].split()[-1] + ')') if lines else print('[STOPPED]  Run start.bat to launch.')"
echo.
pause
