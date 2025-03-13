import joblib
import numpy as np

MODEL_PATH = "models/air_quality_model.pkl"

def load_model():
    """Load the pre-trained model."""
    try:
        model = joblib.load(MODEL_PATH)
        print("✅ Model loaded successfully!")
        return model
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None

def predict_aqi(model, data):
    """Predict AQI based on input features."""
    try:
        # Convert input dictionary to feature array
        features = np.array([list(data.values())]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)
        return float(prediction[0])  # Convert NumPy float to regular float
    except Exception as e:
        print(f"❌ Prediction error: {e}")
        return None
