from fastapi import FastAPI
from .import models
from .database import engine
from .routers import User, Restaurant, menu, login


app = FastAPI()
app.include_router(User.router)
app.include_router(Restaurant.router)

app.include_router(menu.router)
app.include_router(login.router)
models.Base.metadata.create_all(engine)
