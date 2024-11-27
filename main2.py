import logging
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests

# Configuração do logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


API_KEY = "8e20087c6d1fa3d1ffa71e3592d93e54"
GEOCODE_URL = "http://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    logger.info("Página inicial acessada")
    return templates.TemplateResponse("index.html", {"request": request})



# COMANDO PARA SUBIR O SERVIDOR
# uvicorn main:app --reload