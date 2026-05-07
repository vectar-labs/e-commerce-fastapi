from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from schema import ProductCreate, ProductRead
from crud.product_crud import create_product, get_all_products, get_product_by_id
from core.db import get_session


router = APIRouter() 

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductRead)
async def create_product_endpoint(product_data: ProductCreate, session: AsyncSession = Depends(get_session)):
    new_product = await create_product(product_data, session)
    return new_product


@router.get("/", response_model=List[ProductRead])
async def get_all_products_endpoint(session: AsyncSession = Depends(get_session)):
    products = await get_all_products(session=session)
    return products


@router.get("/{product_id}", response_model=ProductRead)
async def get_product_by_id_endpoint(product_id: int, session: AsyncSession = Depends(get_session)):
    product = await get_product_by_id(product_id, session)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product
