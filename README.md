# vector-editor

A web-based recoil vector editor. Runs as a local server — open from any browser on your network. Built to run on a Raspberry Pi or any machine alongside your game setup.

## Stack

- **Backend:** Python / FastAPI
- **Frontend:** Single-file HTML/CSS/JS — no build step
- **Patterns (Vectors):** Plain `.txt` files, one `x,y,ms` per line — editable in Notepad

## Quick Start (Windows)

```
install.bat   ← run once to install dependencies
start.bat     ← start the server
```

Open `http://localhost:8000` in your browser.

## Quick Start (Linux / Raspberry Pi)

```bash
chmod +x install.sh start.sh
./install.sh
./start.sh
```

Open `http://<device-ip>:8000` from any device on your network.

To find your device IP:
```bash
hostname -I
```

## Pattern Format (Vectors)

Patterns are the recoil compensation vectors used by Cearum. Each line represents one shot:

```
# x (left/right),  y (up/down),  duration_ms
0,1,100
-0.3,3.6,100
1.4,3,100
```

Patterns (vectors) are stored in `patterns/<game>/<weapon>.txt` and are fully compatible with [Cearum](https://github.com/yourrepo/cearum)'s `saved_scripts` format.

## Controls

| Action | Control |
|--------|---------|
| Add shot | Click canvas |
| Move shot | Drag dot |
| Delete shot | Right-click dot (short press) |
| Pan canvas | Right-click drag / Space+drag / Middle mouse |
| Zoom in | Scroll up |
| Zoom out | Scroll down |
| Fit all shots in view | Fit All button |
| Delete row | Shift+Delete in table |
| Next row (same column) | Enter |
| Navigate rows | ↑ ↓ arrow keys |

## Project Structure

```
vector-editor/
├── app.py              ← FastAPI backend
├── static/
│   └── index.html      ← entire frontend (self-contained)
├── patterns/           ← saved vectors/patterns (created on first save)
│   └── cs2/
│       └── ak47.txt    ← example vector file
├── requirements.txt
├── start.bat / start.sh
├── stop.bat  / stop.sh
├── status.bat
└── install.bat / install.sh
```

## Server Management (Windows)

```
start.bat    ← start (kills any existing instance on port 8000 first)
stop.bat     ← stop
status.bat   ← check if running and show PID
```

## Server Management (Linux / Raspberry Pi)

```bash
# Start
./start.sh

# Stop
pkill -f "python3 app.py"

# Check if running
pgrep -a -f "app.py"

# Check port
ss -tlnp | grep 8000

# Run in background (survives terminal close)
nohup python3 app.py &> recoil.log &

# Stop background instance
pkill -f "app.py"

# View logs (if running in background)
tail -f recoil.log
```

### Auto-start on boot (Raspberry Pi — systemd)

Create `/etc/systemd/system/vector-editor.service`:

```ini
[Unit]
Description=Vector Editor
After=network.target

[Service]
WorkingDirectory=/home/pi/vector-editor
ExecStart=/usr/bin/python3 app.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

Then enable it:

```bash
sudo systemctl enable vector-editor
sudo systemctl start vector-editor
sudo systemctl status vector-editor
```
