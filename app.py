from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Define the expected features
EXPECTED_FEATURES = ["PM2.5", "PM10", "NO2", "CO", "SO2", "O3", "NH3", 
                     "Temperature", "Humidity", "WindSpeed", "Pressure", 
                     "Latitude", "Longitude", "DayOfWeek", "HourOfDay"]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "AQI Prediction API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Ensure JSON input
        data = request.get_json()
        if not data or "features" not in data:
            return jsonify({"error": "Missing 'features' in request"}), 400
        
        # Extract features
        features = data["features"]

        # Validate input length
        if len(features) != len(EXPECTED_FEATURES):
            return jsonify({"error": f"Expected {len(EXPECTED_FEATURES)} features, got {len(features)}"}), 400
        
        # Convert to NumPy array & reshape for model
        input_data = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_data)

        # Return prediction
        return jsonify({"prediction": prediction.tolist()})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
