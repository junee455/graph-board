from typing import List
from app.domain.entities.card import Card
from app.domain.repositories.card_repository import CardRepository

class CreateCardCommand:   # dtо
    def __init__(self, name: str, description: str, tags: List[str] = None):
        self.name = name
        self.description = description
        self.tags = tags or []

class CreateCardUseCase:
    def __init__(self, card_repository: CardRepository):
        self.card_repository = card_repository
    
    def execute(self, command: CreateCardCommand) -> Card:
        if not command.name.strip():
            raise ValueError("Название карточки не может быть пустым")
        
        card = Card(
            name=command.name.strip(),
            description=command.description.strip(),
            tags=command.tags
        )
        
        return self.card_repository.save(card)