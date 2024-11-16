from typing import List

from fastapi import HTTPException
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette import status

from models import Dog
from schemas import DogCreate


async def get_dog_by_id(
    session: AsyncSession, dog_id: int
):
    stmt = select(Dog).where(Dog.id == dog_id)
    result: Result = await session.execute(stmt)
    dog = result.scalars().one_or_none()

    if dog is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dog с ID ({dog_id}) не найдена",
        )
    return dog


async def create_dog(
    session: AsyncSession, dog_create: DogCreate
):
    dog = Dog(**dog_create.model_dump())
    session.add(dog)
    await session.commit()
    await session.refresh(dog)
    return dog


async def delete_dog(
     session: AsyncSession, dog: Dog
):
     await session.delete(dog)
     await session.commit()
     return dog


async def get_all_dogs(session: AsyncSession) -> List[Dog]:
    stmt = select(Dog)
    result: Result = await session.execute(stmt)
    dogs = result.scalars().all()
    return list(dogs)
