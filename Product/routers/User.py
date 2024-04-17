from fastapi import APIRouter
from ..import schemas
from ..import models
from ..database import engine, get_db
from fastapi import status, Response, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
from .login import get_current_user

router = APIRouter(tags=['User'])


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/users', response_model=schemas.DisplayUser)
def create_seller(request: schemas.User, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    hashed_password = pwd_context.hash(request.password)
    new_user = models.User(
        username=request.username, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/users')
def get_user(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.get('/users/{id}', response_model=schemas.DisplayUser)
def get_user(id: int, db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.user_id == id).first()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, details='product not found')
    return users


@router.delete('/users/{id}')
def update_users(id: int, request: schemas.User, db: Session = Depends(get_db)):
    deleted = db.query(models.User).filter(
        models.User.user_id == id).delete(synchronize_session=False)
    db.commit()
    return {'Product deleted'}


@router.put('/users/{id}')
def update_user(id: int, request: schemas.User, db: Session = Depends(get_db)):
    update_user = db.query(models.User).filter(
        models.User.user_id == id).update(request.dict())
    # if not User.first():
    #     pass
    # User.update(request.dict())
    db.commit()
    return {'product successfully updated'}
