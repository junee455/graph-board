from typing import List
from domain.entities.card import Card
from domain.repositories.card_repository import CardRepository

class GetCardsCommand:
    def __init__(self, filters: dict = None):  # можно добавить фильтры в будущем
        self.filters = filters or {}

class GetCardsUseCase:
    def __init__(self, card_repository: CardRepository):
        self.card_repository = card_repository
    
    def execute(self, command: GetCardsCommand = None) -> List[Card]:  
        # пока игнорируем фильтры, но в будущем можно использовать
        return self.card_repository.get_all()