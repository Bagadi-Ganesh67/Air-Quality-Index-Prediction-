import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# ✅ Load dataset
data_path = "models/air quality index data.csv"  # Ensure this path is correct!
try:
    data = pd.read_csv(data_path)
    print(f"✅ Successfully loaded data with {data.shape[0]} rows and {data.shape[1]} columns.")
except FileNotFoundError:
    print(f"❌ Error: Dataset not found at {data_path}")
    exit()

# ✅ Preprocessing (Replace "AQI" with the actual target column name)
if "AQI" not in data.columns:
    print("❌ Error: 'AQI' column not found in the dataset. Check column names!")
    print("Dataset columns:", data.columns)
    exit()

X = data.drop(columns=["AQI"])
y = data["AQI"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train model
print("🚀 Training model...")
model = RandomForestRegressor()
model.fit(X_train, y_train)
print("✅ Model training complete!")

# ✅ Save trained model
model_path = "models/air_quality_model.pkl"
joblib.dump(model, model_path)
print(f"✅ Model saved successfully at {model_path}")
