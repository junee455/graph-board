#  я решил что выпендриваться с di пока рано - endpoint-ов пока маловато и фабрика там прекрасно справится и без di

#from fastapi import Depends
#from sqlmodel import Session
#from app.domain.repositories.card_repository import CardRepository
#from app.infrastructure.database.repositories.card_repository_impl import PostgreSQLCardRepository
#from app.application.use_cases.cards.create_card import CreateCardUseCase

#def get_card_repository(session: Session) -> CardRepository: 
#    return PostgreSQLCardRepository(session)
#
#def get_create_card_use_case(
#    session: Session  
#) -> CreateCardUseCase:
#    card_repo = get_card_repository(session)
#    return CreateCardUseCase(card_repo)