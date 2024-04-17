from fastapi import APIRouter
from ..import schemas
from ..import models
from ..database import engine, get_db
from fastapi import status, Response, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List
# from passlib.context import CryptContext

router = APIRouter(tags=['Menu'])


@router.post('/menu', response_model=schemas.MenuItem)
def create_menu(request: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    # hashed_password = pwd_context.hash(request.password)
    new_menu = models.MenuItem(restaurant_id=request.restaurant_id,
                               name=request.name, description=request.description, price=request.price)

    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu


@router.get('/menu')
def get_menu(db: Session = Depends(get_db)):
    menu = db.query(models.MenuItem).all()
    return menu


@router.get('/menu/{id}', response_model=schemas.MenuItem)
def get_menu(id: int, db: Session = Depends(get_db)):
    menu = db.query(models.MenuItem).filter(
        models.MenuItem.item_id == id).first()
    if not menu:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, details='product not found')
    return menu


@router.delete('/menu/{id}')
def update_menu(id: int,  db: Session = Depends(get_db)):
    deleted = db.query(models.MenuItem).filter(
        models.MenuItem.item_id == id).delete(synchronize_session=False)
    db.commit()
    return {'Product deleted'}


@router.put('/menu/{id}')
def update_menu(id: int, request: schemas.MenuItem, db: Session = Depends(get_db)):
    update_user = db.query(models.MenuItem).filter(
        models.MenuItem.item_id == id).update(request.dict())
    # if not MenuItem.first():
    #     pass

    db.commit()
    return {'product successfully updated'}
