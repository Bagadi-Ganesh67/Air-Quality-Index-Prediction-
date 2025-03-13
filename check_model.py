import joblib
import os

model_path = "models/air_quality_model.pkl"

# Check if the model file exists
if not os.path.exists(model_path):
    print(f"❌ Error: Model file not found at {model_path}")
else:
    # Load the model
    model = joblib.load(model_path)
    print(f"✅ Model loaded successfully from {model_path}")
    print(f"✅ Model type: {type(model)}")
