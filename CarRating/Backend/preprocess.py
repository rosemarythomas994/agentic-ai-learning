from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import numpy as np
import joblib
import os

app = FastAPI()

# Example categorical mappings - replace or extend as per your trained model
brand_mapping = {"Toyota": 0, "Honda": 1, "Ford": 2}
model_mapping = {"Corolla": 0, "Civic": 1, "F-150": 2}
fuel_mapping = {"Petrol": 0, "Diesel": 1, "Electric": 2, "Hybrid": 3}
transmission_mapping = {"Manual": 0, "Automatic": 1}
accident_mapping = {"No": 0, "Yes": 1}

class VehicleInput(BaseModel):
    brand: str
    model: str
    year: int
    mileage: int
    fuel: str
    transmission: str
    exterior: int
    interior: int
    accident: str
    image: Optional[str] = None

def preprocess_vehicle(vehicle: VehicleInput) -> np.ndarray:
    brand_encoded = brand_mapping.get(vehicle.brand)
    model_encoded = model_mapping.get(vehicle.model)
    fuel_encoded = fuel_mapping.get(vehicle.fuel)
    transmission_encoded = transmission_mapping.get(vehicle.transmission)
    accident_encoded = accident_mapping.get(vehicle.accident)

    # Raise error if any category not found
    if None in [brand_encoded, model_encoded, fuel_encoded, transmission_encoded, accident_encoded]:
        raise ValueError("Unknown category in input features")

    features = np.array([[
        brand_encoded,
        model_encoded,
        vehicle.year,
        vehicle.mileage,
        fuel_encoded,
        transmission_encoded,
        vehicle.exterior,
        vehicle.interior,
        accident_encoded,
    ]])
    return features

# Load the model once on startup
try:
    model_path = os.path.join(os.path.dirname(__file__), "model", "vehicle_model.pkl")
    model = joblib.load(model_path)
except Exception as e:
    print(f"Model loading failed: {e}")
    model = None  # Prevent crashing, handle in endpoint

@app.post("/evaluate")
async def evaluate_vehicle(vehicle: VehicleInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    try:
        features = preprocess_vehicle(vehicle)
        prediction = model.predict(features)[0]
        return {
            "success": True,
            "prediction": float(prediction),
            "message": "Vehicle evaluation successful"
        }
    except ValueError as ve:
        # Input categories mismatch
        return {"success": False, "error": str(ve)}
    except Exception as e:
        # Catch-all for other errors
        return {"success": False, "error": str(e)}
