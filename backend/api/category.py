from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from schema import CategoryCreate, CategoryRead
from crud import category_crud
from core.db import get_session


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategoryRead)
async def create_category_endpoint(category_data: CategoryCreate, session: AsyncSession = Depends(get_session)):
    new_category = await category_crud.create_category(category_data, session)
    return new_category


@router.get("/", response_model=List[CategoryRead])
async def get_all_categories_endpoint(session: AsyncSession = Depends(get_session)):
    categories = await category_crud.get_all_categories(session=session)
    return categories


@router.get("/{category_id}", response_model=CategoryRead)
async def get_category_by_id(category_id: int, session: AsyncSession = Depends(get_session)):
    category = await category_crud.get_category_by_id(category_id, session)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category