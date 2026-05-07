from fastapi import FastAPI
from api import category, product


app = FastAPI(title="E-commerce API", version="1.0")

app.include_router(product.router, prefix="/api/v1/products", tags=["products"])
app.include_router(category.router, prefix="/api/v1/categories", tags=["categories"])