# 📌 Step 1: Load Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 📌 Step 2: Load Dataset
DATA_PATH = "data/processed/air_quality_index_data_processed.csv"  # Update path if necessary

try:
    df = pd.read_csv(DATA_PATH)
    print(f"✅ Dataset Loaded Successfully: {df.shape[0]} rows, {df.shape[1]} columns")
except FileNotFoundError:
    print(f"❌ Error: File not found at {DATA_PATH}")
    df = None

# 📌 Step 3: Display First Few Rows
if df is not None:
    display(df.head())

# 📌 Step 4: Basic Info & Missing Values
if df is not None:
    print("\n🔹 Dataset Info:")
    df.info()
    
    print("\n🔹 Missing Values Count:")
    print(df.isnull().sum())

# 📌 Step 5: Summary Statistics
if df is not None:
    print("\n🔹 Summary Statistics:")
    display(df.describe())

# 📌 Step 6: Visualizing Air Quality Trends

if df is not None:
    # Distribution of AQI
    plt.figure(figsize=(8, 5))
    sns.histplot(df["AQI"], bins=30, kde=True, color="blue")
    plt.title("Distribution of Air Quality Index (AQI)")
    plt.xlabel("AQI")
    plt.ylabel("Frequency")
    plt.show()

    # Boxplot for PM2.5, PM10, NO2
    plt.figure(figsize=(10, 6))
    selected_features = ["PM2.5", "PM10", "NO2"]
    df[selected_features].boxplot()
    plt.title("Boxplot of Key Pollutants")
    plt.show()

    # Correlation Heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Feature Correlation Heatmap")
    plt.show()
    
