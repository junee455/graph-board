from sqlmodel import SQLModel, Field
from typing import List, Optional
from sqlalchemy import Column, JSON
import uuid

class CardModel(SQLModel, table=True):
    __tablename__ = "cards"
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    name: str
    description: str
    status: str = "todo"  # todo, in_progress, done
    tags: List[str] = Field(default=[], sa_column=Column(JSON))
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now().isoformat())