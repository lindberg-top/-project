from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import SessionLocal
from models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@router.post("/")
def created_user(telegram_id: int, db: Session = Depends(get_db)):
    user = User(telegram_id=telegram_id)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return {"message": "user created", "id": {user.id}}


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        return {"message": "user not found"}
    
    return user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        return {"message": "user not found"}
    
    db.delete(user)
    db.commit()
    
    return {"message": "user deleted"}

