from passlib.context import CryptContext
import hashlib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_token(token: str):
    token = hashlib.sha256(token.encode()).hexdigest()
    return pwd_context.hash(token)


def verify_token(plain_token: str, hashed_token: str):
    plain_token = hashlib.sha256(plain_token.encode()).hexdigest()
    
    return pwd_context.verify(plain_token, hashed_token)
