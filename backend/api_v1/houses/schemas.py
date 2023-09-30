from pydantic import BaseModel, ConfigDict, HttpUrl
from datetime import date


from ..apartments.schemas import Apartment


class Image(BaseModel):
    url: HttpUrl
    name: str


class HouseBase(BaseModel):
    street: str
    number: int
    square: float
    number_storeys: int
    number_entrances: int
    year_constraction: date
    #  image: list[Image] | None = None
    apartments: list[Apartment] | None = list[None]


class House(HouseBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class HouseCreate(BaseModel):
    street: str
    number: int
    square: float
    number_storeys: int
    number_entrances: int
    year_constraction: date


class HouseUpdate(HouseCreate):
    pass


class HouseUpdatePartial(HouseCreate):
    street: str | None = None
    number: int | None = None
    square: float | None = None
    number_storeys: int | None = None
    number_entrances: int | None = None
    year_constraction: date | None = None
    image: list[Image] | None = None
