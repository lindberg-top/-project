from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.session import SessionLocal
from backend.app.models.user import User
from backend.app.schemas.user import UserCreate
from backend.app.api.secret_key import generate_key
router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@router.post("/users/")
def created_user(telegram_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if db_user:
        HTTPException(status_code=404, detail="User already exists")
        
    vpn_key = generate_key()
    new_user = User(telegram_id=telegram_id, vpn_key=vpn_key)
    
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"id": {new_user.id}, "telegram_id": {new_user.telegram_id}, "vpn_key": {new_user.vpn_key}}


@router.get("/users/{telegram_id}/vpn_key")
def get_vpn_key(telegram_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if db_user is None:
        HTTPException(status_code=404, detail="User not found")
    
    return {"vpn_key": db_user.vpn_key}

    


@router.delete("/")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        return {"message": "user not found"}
    
    db.delete(user)
    db.commit()
    
    return {"message": "user deleted"}

