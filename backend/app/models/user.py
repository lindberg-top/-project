from sqlalchemy import Column, Integer, BigInteger, String
from backend.app.db.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, index=True)
    vpn_key_hash = Column(String, nullable=True)