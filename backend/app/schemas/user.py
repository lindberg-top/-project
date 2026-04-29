from pydantic import BaseModel

class UserCreate(BaseModel):
    telegram_id: int
    
    
class UserResponse(BaseModel):
    id: int
    telegram_id: int
    
    class Config:
        from_attributes = True