from sqlmodel import SQLModel, create_engine, Session
from fastapi import FastAPI, Depends
from app.infrastructure.database.models import CardModel
from app.infrastructure.api.endpoints import cards
from datetime import datetime


#DATABASE_URL = "postgresql://user:password@localhost/card_db"
DATABASE_URL = "postgresql://user:password@db:5432/card_db"
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine) # создаем таблицы

def get_session():                   # di для работы с бд в FastAPI
    with Session(engine) as session:
        yield session

app = FastAPI(title="Card Board")

app.include_router(cards.router)   # подключаем роутеры

@app.get("/")
async def root():
    return {
        "message": "Card Board proj",
        "version": "1.0.0", 
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()  
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)