import os

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api import routes
from app.core.logging_config import setup_logging
from fastapi import FastAPI, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse

from app.core.config import media_dir

setup_logging()


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/presentations/static"), name='static')
app.mount("/media", StaticFiles(directory='app/presentations/media'), name="media")
templates = Jinja2Templates(directory="app/presentations/templates")


@app.get('/', response_class=HTMLResponse)
async def get_webpage(request: Request):
    return templates.TemplateResponse("main.html", {"request": request, "message": "Contact Us"})


app.include_router(routes.router)


