from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="HORIZON Dashboard", version="2.0.0")
BASE = Path(__file__).resolve().parent
STATIC = BASE / "static"
TEMPLATES = BASE / "templates"

app.mount("/static", StaticFiles(directory=STATIC), name="static")

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return (TEMPLATES / "index.html").read_text(encoding="utf-8")

@app.get("/api/health")
async def health():
    return {
        "name": "HORIZON",
        "status": "online",
        "stage": 2,
        "dashboard": "management-ui"
    }
