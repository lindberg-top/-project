from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://nikola:password@127.0.0.1:5432/vpn_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
