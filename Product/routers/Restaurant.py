from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..import schemas
from ..import models
from typing import List
from ..database import get_db
from fastapi import status, Response, HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from ..schemas import User
# from .login import get_current_user

router = APIRouter(tags=['Restaurant'], prefix="/hotels")


@router.post('/', status_code=status.HTTP_201_CREATED)
def add(request: schemas.Restaurant, db: Session = Depends(get_db)):
    new_hotel = models.Restaurant(
        name=request.name, address=request.address, contact_number=request.contact_number)
    db.add(new_hotel)
    db.commit()
    db.refresh(new_hotel)
    return request


@router.get('/', response_model=List[schemas.Restaurant])
def products(db: Session = Depends(get_db)):
    hotels = db.query(models.Restaurant).all()
    return hotels


@router.get('/{id}', response_model=schemas.Restaurant)
def products(id: int, db: Session = Depends(get_db)):
    hotels = db.query(models.Restaurant).filter(
        models.Restaurant.restaurant_id == id).first()
    if not hotels:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='product not found')
    return hotels


@router.delete('/{id}')
def delete_hotels(id: int, db: Session = Depends(get_db)):
    db.query(models.Restaurant).filter(
        models.Restaurant.restaurant_id == id).delete(synchronize_session=False)
    db.commit()
    return {'Hotel deleted'}


@router.put('/{id}')
def update_hotels(id: int, request: schemas.Restaurant, db: Session = Depends(get_db)):
    updated_hotels = db.query(models.Restaurant).filter(
        models.Restaurant.restaurant_id == id)
    if not updated_hotels.first():
        pass
    updated_hotels.update(request.dict())
    db.commit()
    return {'Restaurant Sucessfully Updated'}
