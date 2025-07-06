import requests
import json

API_URL = "http://18.206.169.206:8000/predict"  # Change if using public IP
API_KEY = "mysecureapikey"

payload = {
    "Client_Income": 200000,
    "Credit_Amount": 150000,
    "Loan_Annuity": 25000,
    "Accompany_Client": "Alone",
    "Client_Income_Type": "Working",
    "Client_Education": "Higher education",
    "Client_Marital_Status": "Married",
    "Client_Gender": "M",
    "Loan_Contract_Type": "Cash loans",
    "Client_Housing_Type": "Rented apartment",
    "Population_Region_Relative": 0.01,
    "Age_Days": -12000,
    "Employed_Days": -3000,
    "Registration_Days": -4000,
    "ID_Days": -1000,
    "Client_Occupation": "Accountants",
    "Client_Permanent_Match_Tag": "Match",
    "Client_Contact_Work_Tag": "Has contact",
    "Type_Organization": "Business Entity Type 3",
    "Score_Source_3": 0.6,
    "ID": 123456,
    "Car_Owned": 0,
    "Bike_Owned": 1,
    "Active_Loan": 0,
    "House_Own": 0,
    "Child_Count": 2,
    "Own_House_Age": 10,
    "Mobile_Tag": 1,
    "Homephone_Tag": 0,
    "Workphone_Working": 1,
    "Client_Family_Members": 3.0,
    "Cleint_City_Rating": 2.0,
    "Application_Process_Day": 15,
    "Application_Process_Hour": 14,
    "Score_Source_1": 0.55,
    "Score_Source_2": 0.60,
    "Social_Circle_Default": 0.1,
    "Phone_Change": 1.0,
    "Credit_Bureau": 0.5
}

headers = {"x-api-key": API_KEY}

res = requests.post(API_URL, json=payload, headers=headers)
print("Status Code:", res.status_code)
print("Response:", res.json())

