from sqlmodel import SQLModel
from typing import Optional, List


class CategoryBase(SQLModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id: int

class UserBase(SQLModel):
    username: str
    email: str
    password: str
    role: Optional[str] = "customer"


class ReviewBase(SQLModel):
    rating: int
    comment: Optional[str] = None
    user_id: int
    product_id: int
    
class ReviewRead(ReviewBase):
    id: int
        

class ProductBase(SQLModel):
    name: str
    description: str
    price: float
 
    
class ProductCreate(ProductBase):
    category_id: int

class ProductRead(ProductBase):
    id: int
    category: CategoryRead
    reviews: List[ReviewRead] = []
