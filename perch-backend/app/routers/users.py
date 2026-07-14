from app.schemas.user import UserResponse, UserCreate
from app.database import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from uuid import UUID
import os

router = APIRouter()
UPLOAD_FOLDER = "uploads/profiles"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.get("/users/{id}", response_model=UserResponse)
def get_user(db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    return user


@router.post("/users", response_model=UserResponse)
def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        first_name=new_user.first_name,
        last_name=new_user.last_name,
        email=new_user.email,
        profile_photo=new_user.profile_photo,
        hashed_password=new_user.hashed_password,
    )
