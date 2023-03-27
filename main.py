import os
from PIL import Image
import torch
from fastapi import FastAPI, Form, File, UploadFile

from config import config
from resnet import resnet18, resnet34, resnet50, resnet101, resnet152, model_setup
from preprocess import imgToTensor


model = model_setup()
prediction_classes = config.prediction_classes
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/liveness/", status_code=200)
def liveness_check():
    return "Liveness check succeeded."

@app.get("/readiness/", status_code=200)
def readiness_check():
    return "Readiness check succeeded."

@app.get("/startup/", status_code=200)
def startup_check():
    return "Startup check succeeded."

@app.get("/predict")
async def predict(image: bytes = File()):
    
    tensor = imgToTensor(image)

    model.eval()
    with torch.inference_mode():
        output = model(tensor)

    _, predicted = torch.max(output.data, 1)
    prediction = prediction_classes[predicted]

    return {"prediction": prediction}
