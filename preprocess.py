import pandas as pd
import os

def load_and_preprocess():
    base_path = r"E:\mturkfitbit_export_4.12.16-5.12.16\Fitabase Data 4.12.16-5.12.16"

    # Get the correct CSV file
    files = [f for f in os.listdir(base_path) if f.endswith(".csv")]
    file_path = os.path.join(base_path, files[0])
    print("📂 Loading file from:", file_path)

    df = pd.read_csv(file_path)

    # Convert date column if present
    if 'ActivityDate' in df.columns:
        df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])

    # Drop non-numeric columns (like dates, strings, IDs)
    df = df.select_dtypes(include=['number'])

    return df
