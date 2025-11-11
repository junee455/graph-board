from app.domain.entities.card import Card, CardStatus
from app.domain.repositories.card_repository import CardRepository

class UpdateCardStatusCommand:
    def __init__(self, card_id: str, status: CardStatus):  # dto
        self.card_id = card_id
        self.status = status

class UpdateCardStatusUseCase:
    def __init__(self, card_repository: CardRepository):
        self.card_repository = card_repository
    
    def execute(self, command: UpdateCardStatusCommand) -> Card:
        card = self.card_repository.get_by_id(command.card_id)
        if not card:
            raise ValueError("Карточка не найдена")
        
        if command.status == CardStatus.TODO: # Используем Enum для простоты валидации 
            card.set_todo()
        elif command.status == CardStatus.IN_PROGRESS:
            card.set_in_progress()
        elif command.status == CardStatus.DONE:
            card.set_done()
        
        return self.card_repository.save(card)