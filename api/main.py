import pandas as pd
import joblib
from fastapi import FastAPI

from schemas import ForecastRequest

app = FastAPI(
    title="Demand Forecasting API",
    version="1.0"
)

model = joblib.load(
    "../models/xgboost_forecasting_model.pkl"
)

inventory_df = pd.read_csv(
    "../processed_data/inventory_recommendations.csv"
)

@app.get("/")
def home():

    return {
        "message":
        "Demand Forecasting & Inventory Optimization API"
    }

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

@app.post("/forecast")
def forecast(
    request: ForecastRequest
):
    
    result = inventory_df[
        (inventory_df["store"] == request.store)
        &
        (inventory_df["item"] == request.item)
    ]

    if result.empty:

        return {
            "error":
            "Store-Item combination not found"
        }
    
    row = result.iloc[0]

    return {
        "store": int(row["store"]),

        "item": int(row["item"]),

        "forecast_demand":
            round(
                float(
                    row["forecast_demand"]
                ),
                2
            ),

        "reorder_point":
            round(
                float(
                    row["reorder_point"]
                ),
                2
            ),

        "inventory_status":
            row["inventory_status"]
    }