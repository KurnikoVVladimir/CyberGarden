from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from database import Base


class Dog(Base):
    __tablename__ = "dogs"

    name: Mapped[str] = mapped_column()

    age: Mapped[float] = mapped_column()

    species: Mapped[str] = mapped_column()

    price: Mapped[float] = mapped_column()
