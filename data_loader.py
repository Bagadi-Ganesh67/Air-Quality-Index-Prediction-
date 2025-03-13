import os
import pandas as pd

# Define the raw data directory
RAW_DATA_DIR = os.path.join("data", "raw")

# Ensure the directory exists
def ensure_raw_data_dir():
    if not os.path.exists(RAW_DATA_DIR):
        os.makedirs(RAW_DATA_DIR)
    print(f"✅ Raw data directory: '{RAW_DATA_DIR}' is ready.")

# List all files in the raw data directory
def list_raw_data_files():
    if not os.path.exists(RAW_DATA_DIR):
        print("❌ Raw data directory does not exist.")
        return []
    
    files = os.listdir(RAW_DATA_DIR)
    if not files:
        print("⚠️ No files found in 'data/raw/'.")
    return files

# Load dataset (CSV or JSON)
def load_raw_data(file_name):
    file_path = os.path.join(RAW_DATA_DIR, file_name)
    
    if not os.path.exists(file_path):
        print(f"❌ File '{file_name}' not found in 'data/raw/'.")
        return None
    
    if file_name.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_name.endswith(".json"):
        return pd.read_json(file_path)
    else:
        print(f"⚠️ Unsupported file format: {file_name}")
        return None

# Example usage
if __name__ == "__main__":
    ensure_raw_data_dir()
    
    # List available raw datasets
    files = list_raw_data_files()
    print("📂 Available raw data files:", files)

    # Load a specific dataset (change file name accordingly)
    file_name = "air_quality_index_data.csv"  # Replace with an actual file name
    if file_name in files:
        df = load_raw_data(file_name)  # ✅ Corrected line
        if df is not None:
            print("✅ Loaded dataset preview:\n", df.head())
