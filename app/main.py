import os

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.logging_config import setup_logging
from fastapi import FastAPI, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse



setup_logging()


media_dir = "media"
os.makedirs(media_dir, exist_ok=True)

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/presentations/static"), name='static')
# app.mount("/media", StaticFiles(directory=media_dir), name="media")
templates = Jinja2Templates(directory="app/presentations/templates")


@app.get('/', response_class=HTMLResponse)
async def get_webpage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Contact Us"})


