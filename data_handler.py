import os
import pandas as pd

DATA_DIR = "data"
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

def create_data_dirs():
    for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR]:
        os.makedirs(directory, exist_ok=True)
    print("✅ Data directories are set up.")

if __name__ == "__main__":
    create_data_dirs()
