from pydantic import BaseModel
from typing import List
from datetime import datetime
import uuid
from enum import Enum

class CardStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress" 
    DONE = "done"

class Card(BaseModel):

    # Идентификатор
    id: str
    
    # Основные атрибуты
    name: str
    description: str
    status: CardStatus = CardStatus.TODO
    
    # Теги для организации
    tags: List[str] = []
    
    # Временные метки
    created_at: datetime
    updated_at: datetime
    
    def __init__(self, **data):            #  Aвтоматически генерируем ID и временные метки если их нет
        if 'id' not in data:
            data['id'] = str(uuid.uuid4())
        if 'created_at' not in data:
            data['created_at'] = datetime.now() # пока будет так, потом допилю метод получения локального времени от клиента 
        if 'updated_at' not in data:
            data['updated_at'] = datetime.now()
        super().__init__(**data)


    def set_todo(self):               # тут мы статусы карточек меняем 
        self.status = CardStatus.TODO 
        self.updated_at = datetime.now()
    
    def set_in_progress(self):
        self.status = CardStatus.IN_PROGRESS
        self.update_status = datetime.now()

    def set_done(self):
        self.status = CardStatus.DONE
        self.update_status = datetime.now()

    def add_tag(self, tag: str):        # методы добавления/удаления тегов 
        tag_clean = tag.strip()
        if tag_clean and tag_clean not in self.tags:
            self.tags.append(tag_clean)
            self.updated_at = datetime.now()
    
    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)
            self.updated_at = datetime.now()
