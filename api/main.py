from fastapi import FastAPI

app = FastAPI(
    title="Demand Forecasting API",
    version="1.0"
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