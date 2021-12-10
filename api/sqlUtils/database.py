import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Configure for cloud db
SQL_DATABASE_URI = os.getenv('DB_URI')

engine = create_engine(
    SQL_DATABASE_URI
)
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
