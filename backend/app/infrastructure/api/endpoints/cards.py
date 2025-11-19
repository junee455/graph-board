from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlmodel import Session

from app.infrastructure.database.repositories.card_repository_impl import PostgreSQLCardRepository
from app.application.use_cases.cards.create_card import CreateCardUseCase, CreateCardCommand
from app.application.use_cases.cards.get_cards import GetCardsUseCase
#from app.infrastructure.api.dependencies import get_create_card_use_case  # di пока не нужны
from app.infrastructure.database.session import get_session


router = APIRouter(prefix="/cards", tags=["cards"])

class CardCreateRequest(BaseModel):
    name: str
    description: str
    tags: List[str] = []

class CardResponse(BaseModel):
    id: str
    name: str
    description: str
    status: str
    tags: List[str]
    created_at: str
    updated_at: str


def create_card_repository(session):
    return PostgreSQLCardRepository(session)   


@router.post("/", response_model=CardResponse)
async def create_card(
    request: CardCreateRequest,
    session: Session = Depends(get_session) 
):
    try:
          #отдаем в юз кейс PostgreSQLCardRepository с сессией бд 
        use_case = CreateCardUseCase(create_card_repository(session))
        
        command = CreateCardCommand(
            name=request.name,
            description=request.description,
            tags=request.tags
        )
        
        card = use_case.execute(command)
        
        return CardResponse(
            id=card.id,
            name=card.name,
            description=card.description,
            status=card.status.value,
            tags=card.tags,
            created_at=card.created_at.isoformat(),
            updated_at=card.updated_at.isoformat()
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[CardResponse])
async def get_cards(session: Session = Depends(get_session)):
    try:
        # временно запустил напрямую без юз кейс потому что с ним что то не заработало, сегодня пофикшу 
        card_repo = PostgreSQLCardRepository(session)
        cards = card_repo.get_all() 
        
        return [
            CardResponse(
                id=card.id,
                name=card.name,
                description=card.description,
                status=card.status.value,
                tags=card.tags,
                created_at=card.created_at.isoformat(),
                updated_at=card.updated_at.isoformat()
            )
            for card in cards
        ]
    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(status_code=500, detail=str(e))