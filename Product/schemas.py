# responsible for containing all the pydantic models
# responsible for data validation
from Product.models import User, Restaurant, MenuItem
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    email: str
    password: str
    is_delivery_person: bool


class DisplayUser(BaseModel):
    username: str
    is_delivery_person: bool

    class Config:
        orm_mode: True


class Restaurant(BaseModel):
    name: str
    address: str
    contact_number: str


class RestaurantCreate(Restaurant):
    pass


class Restaurant(Restaurant):
    restaurant_id: int

    class Config:
        orm_mode = True


class MenuItem(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class MenuItemCreate(MenuItem):
    restaurant_id: int


class MenuItem(MenuItem):
    item_id: int
    restaurant_id: int

    class Config:
        orm_mode = True


class login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
