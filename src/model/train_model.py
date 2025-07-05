# src/model/train_model.py

import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# ✅ SET TRACKING URI to Docker MLflow service
mlflow.set_tracking_uri("http://mlflow:5000")

# ✅ Set or create experiment
mlflow.set_experiment("loan-default-prediction")

print("📡 MLflow Tracking URI:", mlflow.get_tracking_uri())

# Load dataset
df = pd.read_csv("data/raw/Dataset.csv", low_memory=False)

# Clean object-type columns
for col in df.columns:
    if df[col].dtype == object:
        df[col] = df[col].astype(str).str.replace(r"[\$,]", "", regex=True)
        df[col] = df[col].replace("", np.nan)

# Try converting to numeric where possible
for col in df.columns:
    try:
        df[col] = pd.to_numeric(df[col])
    except:
        continue

# Separate features and target
X = df.drop("Default", axis=1)
y = df["Default"]

# Drop rows with missing target
X = X[~y.isna()]
y = y[~y.isna()]

# Identify numeric and categorical columns
num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_cols = X.select_dtypes(include=["object"]).columns.tolist()

print("📊 Numerical columns:", num_cols)
print("🧾 Categorical columns:", cat_cols)

# Build transformers
transformers = []

if num_cols:
    transformers.append(
        (
            "num",
            Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            ),
            num_cols,
        )
    )

if cat_cols:
    transformers.append(
        (
            "cat",
            Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    (
                        "encoder",
                        OrdinalEncoder(
                            handle_unknown="use_encoded_value", unknown_value=-1
                        ),
                    ),
                ]
            ),
            cat_cols,
        )
    )

# Column transformer
preprocessor = ColumnTransformer(transformers=transformers)

# Final pipeline
pipeline = Pipeline(
    [
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=100, random_state=42)),
    ]
)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# ✅ Start MLflow run
with mlflow.start_run():
    pipeline.fit(X_train, y_train)
    preds = pipeline.predict(X_test)

    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds)
    roc = roc_auc_score(y_test, pipeline.predict_proba(X_test)[:, 1])

    # ✅ Log parameters, metrics, and model
    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)
    mlflow.log_metric("roc_auc", roc)
    mlflow.sklearn.log_model(pipeline, "model")

    print(f"✅ Training complete - F1: {f1:.4f}, ROC AUC: {roc:.4f}")

# Save model to local filesystem
os.makedirs("models", exist_ok=True)
joblib.dump(pipeline, "models/best_model.pkl")
print("📦 Model saved at: models/best_model.pkl")
