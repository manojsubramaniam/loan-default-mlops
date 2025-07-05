# src/api/api.py

import joblib
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import pandas as pd
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn

# Load the trained pipeline
model = joblib.load("models/best_model.pkl")

# Initialize FastAPI app
app = FastAPI(title="Loan Default Prediction API")

# Enable Prometheus metrics at /metrics
Instrumentator().instrument(app).expose(app)

# API key for basic access control (change it in prod!)
API_KEY = "mysecureapikey"

# Define the input schema
class LoanApplication(BaseModel):
    Client_Income: float
    Credit_Amount: float
    Loan_Annuity: float
    Accompany_Client: str
    Client_Income_Type: str
    Client_Education: str
    Client_Marital_Status: str
    Client_Gender: str
    Loan_Contract_Type: str
    Client_Housing_Type: str
    Population_Region_Relative: float
    Age_Days: float
    Employed_Days: float
    Registration_Days: float
    ID_Days: float
    Client_Occupation: str
    Client_Permanent_Match_Tag: str
    Client_Contact_Work_Tag: str
    Type_Organization: str
    Score_Source_3: float
    ID: int
    Car_Owned: int
    Bike_Owned: int
    Active_Loan: int
    House_Own: int
    Child_Count: int
    Own_House_Age: float
    Mobile_Tag: int
    Homephone_Tag: int
    Workphone_Working: int
    Client_Family_Members: float
    Cleint_City_Rating: float
    Application_Process_Day: int
    Application_Process_Hour: int
    Score_Source_1: float
    Score_Source_2: float
    Social_Circle_Default: float
    Phone_Change: float
    Credit_Bureau: float

# Home route
@app.get("/")
def read_root():
    return {"message": "Loan Default Prediction API is running 🚀"}

# Prediction endpoint with API key check
@app.post("/predict")
def predict(application: LoanApplication, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    input_data = pd.DataFrame([application.dict()])
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]

    return {
        "prediction": int(prediction),
        "probability_of_default": round(proba, 4)
    }

# Only for running locally (not needed in Docker)
if __name__ == "__main__":
    uvicorn.run("src.api.api:app", host="0.0.0.0", port=8000, reload=True)

