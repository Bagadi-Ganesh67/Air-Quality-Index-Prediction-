import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# ✅ Load Dataset
try:
    data = pd.read_csv("air quality index data.csv")  # Ensure the correct file name
    print(f"✅ Successfully loaded data with {data.shape[0]} rows and {data.shape[1]} columns.")
except FileNotFoundError:
    print("❌ Error: File 'air quality index data.csv' not found. Please check the path.")
    exit()

# ✅ Handle Missing Values (Fill or Drop)
data.dropna(inplace=True)

# ✅ Encode Categorical Features
categorical_columns = data.select_dtypes(include=['object']).columns

label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le  # Store the encoder for future use
print("🔄 Categorical features encoded.")

# ✅ Define Features and Target
target_column = 'AQI'  # Ensure 'AQI' exists in the dataset
if target_column not in data.columns:
    print("❌ Error: Target column 'AQI' not found in the dataset.")
    exit()

X = data.drop(columns=[target_column])
y = data[target_column]

# ✅ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"🔀 Data split: {X_train.shape[0]} training rows, {X_test.shape[0]} testing rows.")

# ✅ Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("🚀 Model training completed.")

# ✅ Save Model
with open("model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)
print("💾 Model saved as 'model.pkl'.")

# ✅ Save Label Encoders (for decoding categorical features later)
with open("label_encoders.pkl", "wb") as encoder_file:
    pickle.dump(label_encoders, encoder_file)
print("💾 Label encoders saved as 'label_encoders.pkl'.")
