# src/data/load_data.py

import pandas as pd
import os

def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load dataset from CSV.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded dataframe.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    df = pd.read_csv(file_path)
    return df

