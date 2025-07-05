import streamlit as st
import requests

st.title("Loan Default Prediction")

input_data = {
    "Client_Income": st.number_input("Client Income", value=5000.0),
    "Credit_Amount": st.number_input("Credit Amount", value=15000.0),
    "Loan_Annuity": st.number_input("Loan Annuity", value=1000.0),
    "Accompany_Client": st.selectbox(
        "Accompany Client", ["Alone", "Family", "Partner"]
    ),
    "Client_Income_Type": st.selectbox(
        "Income Type", ["Working", "Commercial associate", "Pensioner"]
    ),
    "Client_Education": st.selectbox(
        "Education", ["Higher education", "Secondary", "Incomplete higher"]
    ),
    "Client_Marital_Status": st.selectbox(
        "Marital Status", ["Single", "Married", "Divorced"]
    ),
    "Client_Gender": st.selectbox("Gender", ["M", "F"]),
    "Loan_Contract_Type": st.selectbox(
        "Loan Contract Type", ["Cash loans", "Revolving loans"]
    ),
    "Client_Housing_Type": st.selectbox(
        "Housing Type", ["House", "With parents", "Rented apartment"]
    ),
    "Population_Region_Relative": st.number_input(
        "Population Region Relative", value=0.01
    ),
    "Age_Days": st.number_input("Age in Days", value=12000.0),
    "Employed_Days": st.number_input("Employed Days", value=-2000.0),
    "Registration_Days": st.number_input("Registration Days", value=-4000.0),
    "ID_Days": st.number_input("ID Days", value=-3000.0),
    "Client_Occupation": st.selectbox(
        "Occupation", ["Laborers", "Core staff", "Managers"]
    ),
    "Client_Permanent_Match_Tag": st.selectbox("Permanent Match Tag", ["Y", "N"]),
    "Client_Contact_Work_Tag": st.selectbox("Contact Work Tag", ["Y", "N"]),
    "Type_Organization": st.selectbox(
        "Type of Organization", ["Business Entity Type 1", "Business Entity Type 2"]
    ),
    "Score_Source_3": st.number_input("Score Source 3", value=0.6),
    "ID": st.number_input("Client ID", value=100001, step=1),
    "Car_Owned": st.selectbox("Owns Car", [0, 1]),
    "Bike_Owned": st.selectbox("Owns Bike", [0, 1]),
    "Active_Loan": st.selectbox("Active Loan", [0, 1]),
    "House_Own": st.selectbox("Owns House", [0, 1]),
    "Child_Count": st.number_input("Number of Children", value=0, step=1),
    "Own_House_Age": st.number_input("Own House Age", value=5.0),
    "Mobile_Tag": st.selectbox("Has Mobile", [0, 1]),
    "Homephone_Tag": st.selectbox("Has Home Phone", [0, 1]),
    "Workphone_Working": st.selectbox("Work Phone Working", [0, 1]),
    "Client_Family_Members": st.number_input("Family Members", value=2.0),
    "Cleint_City_Rating": st.number_input("City Rating", value=2.0),
    "Application_Process_Day": st.selectbox("Application Day", list(range(1, 32))),
    "Application_Process_Hour": st.selectbox("Application Hour", list(range(0, 24))),
    "Score_Source_1": st.number_input("Score Source 1", value=0.65),
    "Score_Source_2": st.number_input("Score Source 2", value=0.7),
    "Social_Circle_Default": st.number_input("Social Circle Default", value=0.1),
    "Phone_Change": st.number_input("Phone Change (days)", value=500.0),
    "Credit_Bureau": st.number_input("Credit Bureau Score", value=0.2),
}

if st.button("Predict"):
    headers = {"x-api-key": "mysecureapikey"}  # 👈 Your correct API key here
    try:
        response = requests.post(
            "http://api:8000/predict", json=input_data, headers=headers
        )
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['prediction']}")
            st.info(
                f"Probability of Default: {result['probability_of_default'] * 100:.2f}%"
            )
        else:
            st.error(f"Error {response.status_code}: {response.json()}")
    except Exception as e:
        st.error(f"Request failed: {e}")
