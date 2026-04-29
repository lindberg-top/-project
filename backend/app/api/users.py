from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db.session import SessionLocal
from backend.app.models.user import User
from backend.app.schemas.user import UserCreate
from backend.app.api.secret_key import generate_key
from backend.app.api.auth import hash_token
from backend.app.db.deps import get_db
import logging
import secrets

router = APIRouter(prefix="/users", tags=["Users"])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

        
@router.post("/")
def created_user(telegram_id: int, db: Session = Depends(get_db)):
    
    
    db_user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
        
    raw_key = generate_key()
    
    hashed_key = hash_token(raw_key)
    
    new_user = User(telegram_id=telegram_id, vpn_key_hash=hashed_key)
    logging.info("User created")
    
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"id": new_user.id, "telegram_id": new_user.telegram_id, "vpn_key": raw_key}


@router.get("/{telegram_id}/vpn_key")
def get_vpn_key(telegram_id: int, db: Session = Depends(get_db)):
    logging.info("Проверить пользователя по тг айди")
    db_user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"vpn_key_hash": db_user.vpn_key_hash}

    
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
