from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="HORIZON Dashboard", version="1.0.0")
BASE = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return (BASE / "templates" / "index.html").read_text(encoding="utf-8")

@app.get("/api/health")
async def health():
    return {"name": "HORIZON", "status": "online", "stage": 1, "dashboard": "starter"}
