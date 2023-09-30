from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship
from datetime import date

from .base import Base

if TYPE_CHECKING:
    from .apartment import Apartment


""" class Image(Base):
    url: Mapped[str]
    name: Mapped[str] """


class House(Base):
    street: Mapped[str]
    number: Mapped[int]
    square: Mapped[float]
    number_storeys: Mapped[int]
    number_entrances: Mapped[int]
    year_constraction: Mapped[date]

    apartments: Mapped[list["Apartment"]] = relationship(
        back_populates="house"
    )  # связь 1 ко многим
    #  image: Mapped[list[str] | None]
    #  apartments: Mapped[list[Apartment]]
