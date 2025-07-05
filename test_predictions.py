import pandas as pd
import requests
import time

# STEP 1: Load the dataset
df = pd.read_csv("data/raw/Dataset.csv")

# STEP 2: Define the required columns expected by the API
required_columns = [
    "Client_Income", "Credit_Amount", "Loan_Annuity", "Accompany_Client",
    "Client_Income_Type", "Client_Education", "Client_Marital_Status",
    "Client_Gender", "Loan_Contract_Type", "Client_Housing_Type",
    "Population_Region_Relative", "Age_Days", "Employed_Days",
    "Registration_Days", "ID_Days", "Client_Occupation",
    "Client_Permanent_Match_Tag", "Client_Contact_Work_Tag",
    "Type_Organization", "Score_Source_3", "ID", "Car_Owned", "Bike_Owned",
    "Active_Loan", "House_Own", "Child_Count", "Own_House_Age",
    "Mobile_Tag", "Homephone_Tag", "Workphone_Working",
    "Client_Family_Members", "Cleint_City_Rating", "Application_Process_Day",
    "Application_Process_Hour", "Score_Source_1", "Score_Source_2",
    "Social_Circle_Default", "Phone_Change", "Credit_Bureau"
]

# STEP 3: Filter and clean the dataset
df = df[required_columns]
df = df.dropna()  # Optional: drop rows with missing values to avoid API errors

# STEP 4: Setup API endpoint
API_URL = "http://localhost:8000/predict"  # Change to your server IP if testing remotely

# STEP 5: Send each row to the API
predictions = []

print(f"Sending {len(df)} records to FastAPI...")

for idx, row in df.iterrows():
    payload = row.to_dict()

    try:
        res = requests.post(API_URL, json=payload, timeout=10)
        if res.status_code == 200:
            result = res.json()
            predictions.append({
                "ID": row["ID"],
                "prediction": result["prediction"],
                "probability_of_default": result["probability_of_default"]
            })
        else:
            print(f"Failed at index {idx}, status code {res.status_code}")
    except Exception as e:
        print(f"Exception at index {idx}: {e}")
    
    time.sleep(0.1)  # Avoid overloading API

# STEP 6: Save to CSV
output_df = pd.DataFrame(predictions)
output_df.to_csv("predictions.csv", index=False)
print("✅ Predictions saved to predictions.csv")

