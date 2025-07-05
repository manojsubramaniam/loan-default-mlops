from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("models/best_model.pkl")

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"default_prediction": int(prediction[0])}
from prometheus_client import Counter, start_http_server
start_http_server(9000)
prediction_counter = Counter("loan_predictions", "Number of predictions")

@app.post("/predict")
def predict(data: dict):
    prediction_counter.inc()
    ...
from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

model = joblib.load("models/best_model.pkl")  # use your trained model path

class LoanInput(BaseModel):
    feature1: float
    feature2: float
    # Add all expected features based on your dataset

app = FastAPI()

@app.post("/predict")
def predict(input_data: LoanInput):
    df = pd.DataFrame([input_data.dict()])
    pred = model.predict(df)[0]
    return {"prediction": int(pred)}
from prometheus_client import Counter, start_http_server
import time

# Start Prometheus metrics server
start_http_server(9000)
request_counter = Counter("predictions_total", "Total prediction requests")

@app.post("/predict")
def predict(input_data: LoanInput):
    request_counter.inc()
    ...

