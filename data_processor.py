import os
import pandas as pd

# Define paths
RAW_DATA_DIR = os.path.join("data", "raw")
PROCESSED_DATA_DIR = os.path.join("data", "processed")

# Ensure processed data directory exists
def ensure_processed_data_dir():
    if not os.path.exists(PROCESSED_DATA_DIR):
        os.makedirs(PROCESSED_DATA_DIR)
    print(f"✅ Processed data directory: '{PROCESSED_DATA_DIR}' is ready.")

# Load raw data
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

# Process the data
def process_data(file_name):
    df = load_raw_data(file_name)
    if df is None:
        return
    
    # Example: Fill missing values with median
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Save processed data
    processed_file_name = file_name.replace(".csv", "_processed.csv")
    processed_path = os.path.join(PROCESSED_DATA_DIR, processed_file_name)
    
    df.to_csv(processed_path, index=False)
    print(f"✅ Processed data saved as: '{processed_path}'")

# Run processing
if __name__ == "__main__":
    ensure_processed_data_dir()
    
    file_name = "air quality index data.csv"  # Update this with the actual raw data file name
    process_data(file_name)
