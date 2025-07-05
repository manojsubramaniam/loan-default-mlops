import pandas as pd

df = pd.read_csv("data/raw/Dataset.csv", low_memory=False)

# Print all column names
print("COLUMN NAMES:\n")
for col in df.columns:
    print(f"- '{col}'")

