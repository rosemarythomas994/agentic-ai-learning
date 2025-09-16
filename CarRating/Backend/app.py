from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import joblib
import os
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)
app = FastAPI(title="Vehicle Evaluation API")

origins = ["http://localhost:8080", "http://127.0.0.1:8080", "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = os.path.join(os.path.dirname(__file__), "model", "vehicle_model.pkl")
try:
    pipeline = joblib.load(model_path)
    logging.info("Model loaded successfully")
except Exception as e:
    logging.error(f"Failed to load model: {e}")
    pipeline = None

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
    image: Optional[str] = None  # currently unused

@app.get("/")
def root():
    return {"message": "Vehicle Rating Prediction API is running"}

@app.post("/evaluate")
async def evaluate_vehicle(vehicle: VehicleInput):
    if pipeline is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    try:
        data_dict = {
            "brand": [vehicle.brand],
            "model": [vehicle.model],
            "year": [vehicle.year],
            "mileage": [vehicle.mileage],
            "fuel": [vehicle.fuel],
            "transmission": [vehicle.transmission],
            "exterior": [vehicle.exterior],
            "interior": [vehicle.interior],
            "accident": [vehicle.accident]
        }
        
        input_df = pd.DataFrame(data_dict)
        prediction = pipeline.predict(input_df)[0]
        logging.info(f"Model prediction: {prediction}")

        rating = min(max(round(prediction / 4000), 1), 5)
        condition = "Good Condition" if rating >= 4 else "Salvage"
        confidence = 0.92  # example fixed confidence

        if condition == "Good Condition":
            recommended_companies = [
                {"name": "CarTrade", "type": "Dealer", "website": "https://cartrade.com"},
                {"name": "Spinny", "type": "Dealer", "website": "https://spinny.com"},
                {"name": "HDFC Ergo", "type": "Insurance", "website": "https://hdfcergo.com"}
            ]
        else:
            recommended_companies = [
                {"name": "Salvage Yard Ltd", "type": "Salvage Yard", "website": "https://salvageyard.com"},
                {"name": "Insurance Partners", "type": "Insurance", "website": "https://insurancepartner.com"},
                {"name": "Scrap Dealers", "type": "Scrap Dealer", "website": "https://scrapdealers.com"}
            ]

        return {
            "success": True,
            "rating": rating,
            "condition": condition,
            "confidence": confidence,
            "recommended_companies": recommended_companies,
            "message": "Vehicle evaluation successful"
        }

    except Exception as e:
        logging.error(f"Evaluation error: {e}")
        return {"success": False, "error": str(e)}
