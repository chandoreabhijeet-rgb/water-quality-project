# Week 2 - Preprocessing and Model Training

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset (update path if needed)
df = pd.read_csv("water_potability.csv")

# Step 1: Basic info
print("Initial shape:", df.shape)
print("Missing values:\n", df.isnull().sum())

# Step 2: Handle missing values (fill with median)
df = df.fillna(df.median())

# Step 3: Remove duplicates
print("Duplicates before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates after:", df.duplicated().sum())

# Step 4: Features and target
X = df.drop("Potability", axis=1)
y = df["Potability"]

# Step 5: Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 6: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

print("Final dataset ready ✅")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train distribution:\n", y_train.value_counts())
print("y_test distribution:\n", y_test.value_counts())