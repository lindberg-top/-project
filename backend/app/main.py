from db.session import SessionLocal, engine
from db.base import Base
from models.user import User

Base.metadata.create_all(bind=engine)

db = SessionLocal()

new_user = User(telegram_id=111111)

db.add(new_user)
db.commit()

print("user added!")

db.close()