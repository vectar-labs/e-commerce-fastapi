from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship



class User(SQLModel, table = True):
  id: Optional[int] = Field(default=None, primary_key=True)
  username : str = Field(index=True, unique=True)
  email : str = Field(index=True, unique=True)
  password : str = Field(max_length=255)
  role: str = "customer"
  
  reviews: List["Review"] = Relationship(back_populates="user")
  
class Category(SQLModel, table = True):
  id: Optional[int] = Field(default=None, primary_key=True)
  name: str = Field(index=True, unique=True)
  products: List["Product"] = Relationship(back_populates="category")
  
  
class Review(SQLModel, table = True):
  id: Optional[int] = Field(default=None, primary_key=True)
  rating: int = Field(ge=1, le=5)
  comment: Optional[str] = Field(max_length=255)
  user_id: int = Field(foreign_key="user.id")
  user: "User" = Relationship(back_populates="reviews")
  
  product_id: int = Field(foreign_key="product.id") 
  products: "Product" = Relationship(back_populates="reviews")
  
class Product(SQLModel, table = True):
  id: Optional[int] = Field(default=None, primary_key=True)
  name: str = Field(index=True)
  description : str = Field(max_length=255)
  price : float
  category_id: int = Field(foreign_key="category.id")
  # impelementing the relationship with category and review in lazy loading
  category: "Category" = Relationship(back_populates="products")
  reviews: List["Review"] = Relationship(back_populates="products")


