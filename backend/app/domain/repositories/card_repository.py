from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.card import Card

class CardRepository(ABC):
    @abstractmethod
    def save(self, card: Card) -> Card:
        pass
    
    @abstractmethod
    def get_by_id(self, card_id: str) -> Optional[Card]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Card]:
        pass
    
    @abstractmethod
    def find_by_tag(self, tag: str) -> List[Card]:
        pass