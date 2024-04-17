from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean, DateTime, Text
from .database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_delivery_person = Column(Boolean, default=False)

    # orders = relationship("Order", back_populates="user")


class Restaurant(Base):
    __tablename__ = "restaurants"

    restaurant_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    address = Column(String)
    contact_number = Column(String)

    menu_items = relationship("MenuItem", back_populates="restaurant")


class MenuItem(Base):
    __tablename__ = "menu_items"

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.restaurant_id"))
    name = Column(String)
    description = Column(Text)
    price = Column(Numeric)

    restaurant = relationship("Restaurant", back_populates="menu_items")


# class Order(Base):
#     __tablename__ = "orders"

#     order_id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("users.user_id"))
#     restaurant_id = Column(Integer, ForeignKey("restaurants.restaurant_id"))
#     order_date = Column(DateTime)
#     status = Column(String)
#     delivery_person_id = Column(
#         Integer, ForeignKey("users.user_id"), nullable=True)

#     user = relationship("User", back_populates="orders")
#     items = relationship("OrderItem", back_populates="order")
#     delivery_person = relationship("User", foreign_keys=[delivery_person_id])


# class OrderItem(Base):
#     __tablename__ = "order_items"

#     order_item_id = Column(Integer, primary_key=True, autoincrement=True)
#     order_id = Column(Integer, ForeignKey("orders.order_id"))
#     item_id = Column(Integer, ForeignKey("menu_items.item_id"))
#     quantity = Column(Integer)
#     price = Column(Numeric)

#     order = relationship("Order", back_populates="items")
