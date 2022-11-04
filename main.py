import os
from PIL import Image
import torch
from fastapi import FastAPI, Form, File, UploadFile

from config import config
from resnet import resnet18, resnet34, resnet50, resnet101, resnet152
from preprocess import imgToTensor


def model_setup():
    MODEL_DIR = os.getenv('MODEL_DIR')
    MODEL_FILE = os.getenv('MODEL_FILE')
    MODEL_NAME = os.getenv('MODEL_NAME')
    MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)

    model_dict = model_dict = {'resnet18': resnet18(3,10)
                    ,'resnet34': resnet34(3,10)
                    ,'resnet50': resnet50(3,10)
                    ,'resnet101': resnet101(3,10)
                    ,'resnet152': resnet152(3,10)
                    }

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model_dict[MODEL_NAME]
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))

    return model

model = model_setup()
prediction_classes = config.prediction_classes
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/predict")
async def predict(image: bytes = File()):
    
    tensor = imgToTensor(image)

    model.eval()
    with torch.inference_mode():
        output = model(tensor)

    _, predicted = torch.max(output.data, 1)
    prediction = prediction_classes[predicted]

    return {"prediction": prediction}