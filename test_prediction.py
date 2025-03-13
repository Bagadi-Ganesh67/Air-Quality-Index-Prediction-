import joblib
import numpy as np
import pandas as pd  # ✅ Add this

# Load model
model = joblib.load("models/air_quality_model.pkl")

# Check expected features
feature_names = ["PM2.5", "PM10", "NO", "NO2", "NOx", "NH3", "CO", "SO2", "O3", "Benzene", "Toluene", "Xylene", "AQI"]
print(f"✅ Model expects {model.n_features_in_} features")

# Define sample input as a DataFrame ✅
sample_input = pd.DataFrame([[45, 80, 20, 30, 40, 15, 0.5, 10, 50, 5, 2, 10, 100]], columns=feature_names)

# Predict
prediction = model.predict(sample_input)
print(f"🔹 Predicted AQI: {prediction[0]}")
