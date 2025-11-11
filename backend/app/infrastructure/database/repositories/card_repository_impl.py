from typing import Optional, List  
from datetime import datetime      
from sqlmodel import Session, select
from app.domain.entities.card import Card, CardStatus 
from app.domain.repositories.card_repository import CardRepository
from app.infrastructure.database.models import CardModel

class PostgreSQLCardRepository(CardRepository):
    def __init__(self, session: Session):  
        self.session = session
    
    def save(self, card: Card) -> Card:
        db_card = CardModel(
            id=card.id,
            name=card.name,
            description=card.description, 
            status=card.status.value,
            tags=card.tags,
            created_at=card.created_at.isoformat(),
            updated_at=card.updated_at.isoformat()
        )
        
        self.session.add(db_card)
        self.session.commit()
        return card  
    
    def get_by_id(self, card_id: str) -> Optional[Card]:
        db_card = self.session.get(CardModel, card_id)
        if db_card:
            return self._to_domain(db_card)
        return None

    def get_all(self) -> List[Card]:
        db_cards = self.session.exec(select(CardModel)).all()
        return [self._to_domain(card) for card in db_cards]
    
    def find_by_tag(self, tag: str) -> List[Card]:  
        db_cards = self.session.exec(select(CardModel)).all()
        return [self._to_domain(card) for card in db_cards if tag in card.tags]
    
    def _to_domain(self, db_card: CardModel) -> Card:
        return Card(
            id=db_card.id,
            name=db_card.name,
            description=db_card.description,
            status=CardStatus(db_card.status),  # string → Enum
            tags=db_card.tags,
            created_at=datetime.fromisoformat(db_card.created_at),
            updated_at=datetime.fromisoformat(db_card.updated_at)
        )