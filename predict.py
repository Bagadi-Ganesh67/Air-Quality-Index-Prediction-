import pickle
import numpy as np
import pandas as pd

# Load the trained model
def load_model(model_path):
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        print(f"✅ Model loaded from '{model_path}'")
        return model
    except FileNotFoundError:
        print(f"❌ Error: Model file not found: {model_path}")
        exit()
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        exit()

# Load feature names from processed data
def get_feature_names(processed_data_path):
    try:
        df = pd.read_csv(processed_data_path)
        feature_names = list(df.columns[:-1])  # Excluding the target column
        print(f"✅ Expected {len(feature_names)} features: {feature_names}")
        return feature_names
    except FileNotFoundError:
        print(f"❌ Error: Processed data file not found: {processed_data_path}")
        exit()
    except Exception as e:
        print(f"❌ Error reading processed data: {e}")
        exit()

# Make predictions
def predict(model, feature_names, input_features):
    if len(input_features) != len(feature_names):
        print(f"❌ Error: Expected {len(feature_names)} features, but got {len(input_features)}.")
        exit()
    
    input_df = pd.DataFrame([input_features], columns=feature_names)
    prediction = model.predict(input_df)
    print(f"📈 Predicted AQI: {prediction[0]}")
    return prediction[0]

if __name__ == "__main__":
    MODEL_PATH = "models/air_quality_model.pkl"
    FEATURES_FILE = "data/processed/air quality index data_processed.csv"

    
    model = load_model(MODEL_PATH)
    feature_names = get_feature_names("data/processed/air quality index data_processed.csv")


    
    # Example input (should match the number of features expected)
    input_features = ["City_Name", "2025-03-12", 30, 45, 78, 12, 56, 5.6, 1.2, 4.5, 3.1, 10.5, 7.8, 2.3, 4.0]

    
    predict(model, feature_names, input_features)
