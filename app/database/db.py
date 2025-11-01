from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

SQL_ALCHEMY_DB= os.getenv("SQL_ALCHEMY_DB")

engine = create_engine(SQL_ALCHEMY_DB)
SessionLocal = sessionmaker(autcommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()
