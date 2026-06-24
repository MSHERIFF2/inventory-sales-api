from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/products",
    tags = ["Products"],
)

class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100, description="Name of the product")
    price: float = Field(gt=0, description="Price of the product")
    quantity: int = Field(ge=0, description="Available quantity of the product")

class Product(ProductCreate):
    id: int 

products: list[Product] = [] 
next_product_id = 1 

@router.get("/", response_model=list[Product])
def get_products():
    return products

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")  

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    global next_product_id
    new_product = Product(id=next_product_id, **product.model_dump())
    products.append(new_product)
    next_product_id += 1
    return new_product

@router.put("/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
def update_product(product_id: int, product: ProductCreate):
    for i, existing_product in enumerate(products):
        if existing_product.id == product_id:
            products[i] = Product(id=product_id, **product.model_dump())
            return products[i]
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    for i, existing_product in enumerate(products):
        if existing_product.id == product_id:
            del products[i]
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")