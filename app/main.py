from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version


app = FastAPI()


class descriptionIn(BaseModel):
    description: str


class PredictionOut(BaseModel):
    codigo: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: descriptionIn):
    codigo = predict_pipeline(payload.description)
    return {"codigo": codigo}
