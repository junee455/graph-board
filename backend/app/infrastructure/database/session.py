from sqlmodel import Session, create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/card_db")
engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session