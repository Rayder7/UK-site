from sqlalchemy.orm import Mapped

from .mixin import HouseRelationMixin
from .base import Base


class Apartment(HouseRelationMixin, Base):
    _house_back_populates = "apartments"

    number: Mapped[int]
    floor: Mapped[int]
    entrance: Mapped[int]
    square_apart: Mapped[float]
