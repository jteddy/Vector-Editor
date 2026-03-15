# recoil-editor

A web-based recoil pattern editor. Runs as a local server — open from any browser on your network. Built to run on a Raspberry Pi or any machine alongside your game setup.

## Stack

- **Backend:** Python / FastAPI
- **Frontend:** Single-file HTML/CSS/JS — no build step
- **Patterns:** Plain `.txt` files, one `x,y,ms` per line — editable in Notepad

## Quick Start (Windows)

```
install.bat   ← run once to install dependencies
start.bat     ← start the server
```

Open `http://localhost:8000` in your browser.

## Quick Start (Linux / Raspberry Pi)

```bash
./install.sh
./start.sh
```

Open `http://<device-ip>:8000` from any device on your network.

## Pattern Format

Each line is a shot: `x, y, duration_ms`

```
0,1,100
-0.3,3.6,100
1.4,3,100
```

Patterns are stored in `patterns/<game>/<weapon>.txt` and are fully compatible with [Cearum](https://github.com/yourrepo/cearum)'s `saved_scripts` format.

## Controls

| Action | Control |
|--------|---------|
| Add shot | Click canvas |
| Move shot | Drag dot |
| Delete shot | Right-click dot (short press) |
| Pan canvas | Right-click drag / Space+drag / Middle mouse |
| Zoom | Scroll wheel or slider |
| Fit all shots | Fit All button |
| Delete row | Shift+Delete in table |
| Navigate rows | Enter / ↑ ↓ arrows |

## Project Structure

```
recoil-editor/
├── app.py              ← FastAPI backend
├── static/
│   └── index.html      ← entire frontend (self-contained)
├── patterns/           ← saved patterns (created on first save)
│   └── cs2/
│       └── ak47.txt
├── requirements.txt
├── start.bat / start.sh
├── stop.bat
├── status.bat
└── install.bat / install.sh
```

## Server Management (Windows)

```
start.bat    ← start (kills existing instance on port 8000 first)
stop.bat     ← stop
status.bat   ← check if running
```
