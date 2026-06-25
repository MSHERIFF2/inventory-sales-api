from fastapi import FastAPI
from app.routers import products
from app.database import Base, engine
# from app.models.products import Product

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Inventory Sales API",
    version="1.0.0",
    description="Backend API for managing inventory and sales data, providing endpoints for CRUD operations and analytics.  ",
)
app.include_router(products.router)

# @app.get("/health", tags=["Health Check"])
# def health_check():
#     return {"status": "healthy", "message": "Inventory Sales API is running smoothly."}

