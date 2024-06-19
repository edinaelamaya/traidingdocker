from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from tensorflow.keras.models import load_model
from typing import List
import base64
import cv2
import numpy as np
import io
from PIL import Image
import os

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

# Cargar el modelo de lenguaje de señas
model_path = os.path.join(os.getcwd(), "app/sign_language_model.h5")
model = load_model(model_path)

# Middleware CORS, rutas de documentos y nombres
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas de los documentos
# Asumiendo que estos son los nombres correctos de los routers
from app.routers.docs import docs
from app.routers.get_data import get_nombre

app.include_router(docs)
app.include_router(get_nombre)

# Montar archivos estáticos y plantillas de Jinja2
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Función para preprocesar la imagen
def preprocess_image(image):
    # Convertir imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Redimensionar la imagen para que coincida con la forma de entrada del modelo
    resized = cv2.resize(gray, (28, 28))
    # Normalizar la imagen
    normalized = resized / 255.0
    # Reorganizar la imagen para la entrada del modelo (agregar dimensión de lote)
    reshaped = normalized.reshape(1, 28, 28, 1)
    return reshaped

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Clase para manejar datos de imagen
class ImageData(BaseModel):
    image: str

def predict_letter(image):
    image = cv2.resize(image, (150, 150))
    image = np.expand_dims(image, axis=0)
    image = image / 255.0

    prediction = model.predict(image)
    predicted_letter_index = np.argmax(prediction)

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    predicted_letter = alphabet[predicted_letter_index]

    return predicted_letter

# Endpoint para la predicción
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    print("imagen")
    image = Image.open(io.BytesIO(await file.read()))
    image = np.array(image)  # Convertir a numpy array
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convertir de RGB a BGR
    letter = predict_letter(image)
    return {"predicted_class": ord(letter) - 65}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
