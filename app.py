"""
Vector Editor — Web Backend
------------------------------------
FastAPI server that:
  - Serves the web UI at http://0.0.0.0:8000
  - Manages pattern CRUD (.txt files in ./patterns/<game>/<weapon>.txt)

Pattern format (x,y,ms per line):
    0,1,100
    -0.3,3.6,100

Run:
    python app.py

Then open http://<device-ip>:8000 from any browser on your network.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, PlainTextResponse
import os

app = FastAPI(title="Vector Editor")

PATTERNS_DIR = os.path.join(os.path.dirname(__file__), "patterns")
os.makedirs(PATTERNS_DIR, exist_ok=True)

# ── Pattern API (.txt, x,y,ms per line) ───────────────────────────────────────

@app.get("/api/patterns")
def list_patterns():
    """Return all patterns grouped by game."""
    result = {}
    for game in sorted(os.listdir(PATTERNS_DIR)):
        gp = os.path.join(PATTERNS_DIR, game)
        if not os.path.isdir(gp):
            continue
        weapons = [f[:-4] for f in sorted(os.listdir(gp))
                   if f.endswith(".txt")]
        if weapons:
            result[game] = weapons
    return result


@app.get("/api/patterns/{game}/{weapon}")
def get_pattern(game: str, weapon: str):
    """Load a pattern — returns raw x,y,ms lines."""
    path = os.path.join(PATTERNS_DIR, game, f"{weapon}.txt")
    if not os.path.exists(path):
        raise HTTPException(404, "Pattern not found")
    with open(path) as f:
        return PlainTextResponse(f.read())


@app.post("/api/patterns/{game}/{weapon}")
async def save_pattern(game: str, weapon: str, request: Request):
    """Save a pattern — body is raw x,y,ms lines."""
    body = await request.body()
    folder = os.path.join(PATTERNS_DIR, game)
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{weapon}.txt")
    with open(path, "w") as f:
        f.write(body.decode())
    return {"saved": True, "path": f"{game}/{weapon}"}


@app.delete("/api/patterns/{game}/{weapon}")
def delete_pattern(game: str, weapon: str):
    """Delete a pattern."""
    path = os.path.join(PATTERNS_DIR, game, f"{weapon}.txt")
    if not os.path.exists(path):
        raise HTTPException(404, "Pattern not found")
    os.remove(path)
    gp = os.path.join(PATTERNS_DIR, game)
    if not os.listdir(gp):
        os.rmdir(gp)
    return {"deleted": True}



# ── Serve frontend ────────────────────────────────────────────────────────────

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def index():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


if __name__ == "__main__":
    import uvicorn
    print("\n================================")
    print(" Vector Editor")
    print(" http://localhost:8000")
    print(" Ctrl+C to stop")
    print("================================\n")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
