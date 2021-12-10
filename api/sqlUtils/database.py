from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configure for cloud db
SQL_DATABASE_URI = 'postgresql://xfsgwvgmhhhvco:886d96f20eb1ec6db0c7196aa6cc469f555983eff74827a792652de7500977b9@ec2-107-22-83-3.compute-1.amazonaws.com:5432/d5l5861bl1m4uh'

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
