from pydantic import BaseModel, ConfigDict, HttpUrl
from datetime import date


from ..apartments.schemas import Apartment


class Image(BaseModel):
    url: HttpUrl
    name: str


class BuildingBase(BaseModel):
    street: str
    number: str
    square: float
    number_storeys: int
    number_entrances: int
    year_constraction: date
    #  image: list[Image] | None = None
    apartments: list[Apartment] | None = list[None]


class Building(BuildingBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class BuildingCreate(BaseModel):
    street: str
    number: str
    square: float
    number_storeys: int
    number_entrances: int
    year_constraction: date


class BuildingUpdate(BuildingCreate):
    pass


class BuildingUpdatePartial(BuildingCreate):
    street: str | None = None
    number: str | None = None
    square: float | None = None
    number_storeys: int | None = None
    number_entrances: int | None = None
    year_constraction: date | None = None
    image: list[Image] | None = None
