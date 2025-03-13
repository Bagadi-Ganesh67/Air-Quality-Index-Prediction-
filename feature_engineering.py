import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Define paths
PROCESSED_DATA_DIR = os.path.join("data", "processed")
FEATURED_DATA_DIR = os.path.join("data", "featured")

# Ensure featured data directory exists
def ensure_featured_data_dir():
    if not os.path.exists(FEATURED_DATA_DIR):
        os.makedirs(FEATURED_DATA_DIR)
    print(f"✅ Featured data directory: '{FEATURED_DATA_DIR}' is ready.")

# Load processed data
def load_processed_data(file_name):
    file_path = os.path.join(PROCESSED_DATA_DIR, file_name)
    
    if not os.path.exists(file_path):
        print(f"❌ File '{file_name}' not found in 'data/processed/'.")
        return None
    
    return pd.read_csv(file_path)

# Feature selection & transformation
def feature_engineering(file_name):
    df = load_processed_data(file_name)
    if df is None:
        return
    
    print("📊 Performing feature engineering...")

    # Drop unnecessary columns (example: dropping 'ID' or non-relevant columns)
    if 'ID' in df.columns:
        df.drop(columns=['ID'], inplace=True)

    # Handle categorical variables (convert to numeric if needed)
    df = pd.get_dummies(df)

    # Normalize numerical features
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    scaler = StandardScaler()  # You can also use MinMaxScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Save the transformed dataset
    featured_file_name = file_name.replace("_processed.csv", "_featured.csv")
    featured_path = os.path.join(FEATURED_DATA_DIR, featured_file_name)
    
    df.to_csv(featured_path, index=False)
    print(f"✅ Featured data saved as: '{featured_path}'")

# Run feature engineering
if __name__ == "__main__":
    ensure_featured_data_dir()
    
    file_name = "air quality index data_processed.csv"  # Update if needed
    feature_engineering(file_name)
