from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, scoped_session
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///rfq.db")

class Base(DeclarativeBase):
    pass

# sqlite needs check_same_thread=False for Flask dev server
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))
