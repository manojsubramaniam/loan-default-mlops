# src/data/preprocess.py

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def preprocess_data(df: pd.DataFrame, target_col: str):
    """
    Splits features/target, builds preprocessing pipeline.
    
    Returns:
        X_preprocessed: Preprocessed features
        y: Target variable
        preprocessor: Fitted pipeline (for inference)
    """
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Identify types
    numerical_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()

    # Pipelines
    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    # Combine
    preprocessor = ColumnTransformer([
        ("num", numeric_pipeline, numerical_cols),
        ("cat", categorical_pipeline, categorical_cols)
    ])

    X_preprocessed = preprocessor.fit_transform(X)

    return X_preprocessed, y, preprocessor

