from fastapi import FastAPI

app = FastAPI(
    title="Inventory Sales API",
    version="1.0.0",
    description="Backend API for managing inventory and sales data, providing endpoints for CRUD operations and analytics.  ",
)

@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "healthy", "message": "Inventory Sales API is running smoothly."}

