# src/features/build_features.py

import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create or transform features here before preprocessing.

    Args:
        df (pd.DataFrame): Raw or cleaned input data

    Returns:
        pd.DataFrame: Feature-enhanced DataFrame
    """

    df = df.copy()

    # Example: Create a new feature
    if "loan_amount" in df.columns and "term" in df.columns:
        df["loan_per_term"] = df["loan_amount"] / df["term"].replace(0, 1)

    # Example: Convert date columns to datetime if any
    if "issue_date" in df.columns:
        df["issue_date"] = pd.to_datetime(df["issue_date"])
        df["issue_year"] = df["issue_date"].dt.year
        df["issue_month"] = df["issue_date"].dt.month

    # You can add more domain-specific features here

    return df

