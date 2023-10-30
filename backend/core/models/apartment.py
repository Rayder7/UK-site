from sqlalchemy.orm import Mapped

from .mixin import BuildingRelationMixin
from .base import Base


class Apartment(BuildingRelationMixin, Base):
    _house_back_populates = "apartments"

    number: Mapped[int]
    floor: Mapped[int]
    entrance: Mapped[int]
    square_apart: Mapped[float]
