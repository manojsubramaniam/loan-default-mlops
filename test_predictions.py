import requests

def test_api_predict():
    sample_data = {
        "Client_Income": 25000,
        "Credit_Amount": 500000,
        "Loan_Annuity": 15000,
        "Accompany_Client": "Relative",
        "Client_Income_Type": "Working",
        "Client_Education": "Higher education",
        "Client_Marital_Status": "Single / not married",
        "Client_Gender": "M",
        "Loan_Contract_Type": "Cash loans",
        "Client_Housing_Type": "House / apartment",
        "Population_Region_Relative": 0.005,
        "Age_Days": -12000,
        "Employed_Days": -3000,
        "Registration_Days": -4000,
        "ID_Days": -2500,
        "Client_Occupation": "Laborers",
        "Client_Permanent_Match_Tag": 1,
        "Client_Contact_Work_Tag": 0,
        "Type_Organization": "Business Entity Type 3",
        "Score_Source_3": 0.45,
        "ID": 1,
        "Car_Owned": 1,
        "Bike_Owned": 0,
        "Active_Loan": 0,
        "House_Own": 1,
        "Child_Count": 2,
        "Own_House_Age": 10,
        "Mobile_Tag": 1,
        "Homephone_Tag": 0,
        "Workphone_Working": 1,
        "Client_Family_Members": 3,
        "Cleint_City_Rating": 2,
        "Application_Process_Day": 5,
        "Application_Process_Hour": 12,
        "Score_Source_1": 0.62,
        "Score_Source_2": 0.55,
        "Social_Circle_Default": 0.1,
        "Phone_Change": 100,
        "Credit_Bureau": 3.0
    }

    response = requests.post("http://18.206.169.206:8000/predict", json=sample_data)
    assert response.status_code == 200
    assert "default_probability" in response.json()
