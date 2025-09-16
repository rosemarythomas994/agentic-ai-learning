import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

# Load CSV
df = pd.read_csv("data/vehicles_data.csv")

# Features and target
feature_cols = ["brand", "model", "year", "mileage", "fuel", "transmission", "exterior", "interior", "accident"]
target_col = "price"

X = df[feature_cols]
y = df[target_col]

# Categorical and numeric features
categorical_cols = ["brand", "model", "fuel", "transmission", "accident"]
numeric_cols = ["year", "mileage", "exterior", "interior"]

# Encoder with handling unknown categories for safety during prediction
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown='ignore'), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])

# Fit model
pipeline.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(pipeline, "model/vehicle_model.pkl")

print("Model and encoder saved successfully!")
