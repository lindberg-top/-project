from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from backend.app.api.users import get_db
from backend.app.models.user import User

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    
    user = db.query(User).filter(User.vpn_key == token).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return user 