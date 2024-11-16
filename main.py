import uvicorn
import services

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_manager
from models import *
from typing import List
from schemas import Dog, DogCreate
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel


app = FastAPI(title='Keber_PES')
router = APIRouter()



@router.get(
    path="/dogs/{dog_id}/",
    response_model=Dog,
    description="Собака по айди",
)
async def get_dog_by_id(
    dog_id: int,
    session: AsyncSession = Depends(db_manager.session_dependency),
):
    return await services.get_dog_by_id(session=session, dog_id=dog_id)


@router.post(
    path="/dogs/",
    response_model=Dog,
    description="Создать Собаку",
)
async def create_dog(
    dog_create: DogCreate,
    session: AsyncSession = Depends(db_manager.session_dependency),
):
    return await services.create_dog(
        session=session, dog_create=dog_create
    )

@router.get(
    path="/dogs/",
    response_model=List[Dog],
    description="Все Собаки",
)
async def get_dogs(
    session: AsyncSession = Depends(db_manager.session_dependency)
):
    return await services.get_all_dogs(session)

@router.delete(
    path="/dogs/",
    response_model=Dog,
    description='Vova SOsi'
)
async def delete_dog(
    dog_id: int,
    session: AsyncSession = Depends(db_manager.session_dependency)
):
    dog = await services.get_dog_by_id(session,dog_id)
    return await services.delete_dog(session,dog)




app.include_router(router)