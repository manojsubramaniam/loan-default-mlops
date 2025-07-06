# src/drift_detection/detect_drift.py

import pandas as pd
from evidently.dashboard import Dashboard
from evidently.tabs import DataDriftTab, TestDriftTab

def detect_drift(reference_data_path, current_data_path, output_path='drift_report.html'):
    """
    Detects data drift by comparing the reference data (historical) with the current data.
    
    Parameters:
    - reference_data_path (str): Path to the reference dataset (historical data).
    - current_data_path (str): Path to the current dataset (new/production data).
    - output_path (str): The output path where the drift report will be saved.
    """
    # Load the reference data (historical data)
    reference_data = pd.read_csv(reference_data_path)
    
    # Load the current data (new/production data)
    current_data = pd.read_csv(current_data_path)

    # Initialize the dashboard with the drift detection tabs
    dashboard = Dashboard(tabs=[DataDriftTab(), TestDriftTab()])

    # Calculate drift
    dashboard.calculate(reference_data, current_data)

    # Save the report to an HTML file
    dashboard.save(output_path)
    print(f"Drift report saved to {output_path}")

# Example usage (can be run after training)
if __name__ == "__main__":
    detect_drift(
        reference_data_path="data/raw/Dataset.csv",  # Historical data
        current_data_path="data/processed/current_data.csv",  # Latest data for comparison
        output_path="drift_report.html"  # Output path for the drift report
    )
