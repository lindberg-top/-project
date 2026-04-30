from sqlalchemy import Column, Integer, BigInteger, String, DateTime, Text
from backend.app.db.base import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, index=True)
    vpn_key_hash = Column(Text, nullable=False)
    subscription_until = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)