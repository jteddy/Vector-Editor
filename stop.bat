@echo off
cd /d "%~dp0"
echo Stopping Vector Editor...
python -c "import subprocess; r=subprocess.run('netstat -aon',capture_output=True,text=True); lines=[l for l in r.stdout.splitlines() if ':8000 ' in l and 'LISTENING' in l]; [subprocess.run(f'taskkill /PID {l.split()[-1]} /F',shell=True) for l in lines]; print('Stopped.' if lines else 'No server running on port 8000.')"
pause
