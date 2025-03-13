import os
import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Define paths
MODEL_DIR = os.path.join("models")
FEATURED_DATA_DIR = os.path.join("data", "featured")

# Load the trained model
def load_model(model_name="air_quality_model.pkl"):
    model_path = os.path.join(MODEL_DIR, model_name)
    
    if not os.path.exists(model_path):
        print(f"❌ Model file '{model_name}' not found in 'models/' directory.")
        return None
    
    print(f"✅ Loading model from '{model_path}'...")
    return joblib.load(model_path)

# Load test data
def load_test_data(file_name):
    file_path = os.path.join(FEATURED_DATA_DIR, file_name)
    
    if not os.path.exists(file_path):
        print(f"❌ File '{file_name}' not found in 'data/featured/'.")
        return None
    
    return pd.read_csv(file_path)

# Evaluate the model
def evaluate_model(file_name):
    df = load_test_data(file_name)
    if df is None:
        return
    
    print("📊 Evaluating the model...")

    # Define features (X) and target (y)
    X_test = df.drop(columns=["AQI"])  # Ensure "AQI" is the correct target column
    y_test = df["AQI"]

    # Load trained model
    model = load_model()
    if model is None:
        return

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate model performance
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"📊 Model Evaluation Results:")
    print(f"   - Mean Absolute Error (MAE): {mae:.2f}")
    print(f"   - Mean Squared Error (MSE): {mse:.2f}")
    print(f"   - R² Score: {r2:.2f}")

# Run evaluation
if __name__ == "__main__":
    file_name = "air quality index data_featured.csv"  # Update this if needed
    evaluate_model(file_name)
