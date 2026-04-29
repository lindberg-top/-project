from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.session import SessionLocal
from backend.app.models.user import User
from backend.app.schemas.user import UserCreate
from backend.app.api.secret_key import generate_key
import logging

router = APIRouter(prefix="/users", tags=["Users"])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@router.post("/")
def created_user(telegram_id: int, db: Session = Depends(get_db)):
    logging.info("Created User")
    db_user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if db_user:
        HTTPException(status_code=404, detail="User already exists")
        
    vpn_key = generate_key()
    new_user = User(telegram_id=telegram_id, vpn_key=vpn_key)
    
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"id": {new_user.id}, "telegram_id": {new_user.telegram_id}, "vpn_key": {new_user.vpn_key}}


@router.get("/{telegram_id}/vpn_key")
def get_vpn_key(telegram_id: int, db: Session = Depends(get_db)):
    logging.info("Проверить пользователя по тг айди")
    db_user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if db_user is None:
        HTTPException(status_code=404, detail="User not found")
    
    return {"vpn_key": db_user.vpn_key}

    
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    logger.info(f"Delete request for user_id={user_id}")
    
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        logger.warning(f"user not found: {user_id}")
        return {"error": "User not found"}
    
    db.delete(user)
    db.commit()
    
    logger.info(f"User deleted: {user_id}")
    
    return {"message": "User deleted"}
