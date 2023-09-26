from pydantic import BaseModel, HttpUrl
from datetime import date, datetime


class News(BaseModel):
    name: str
    text: str
    created_date: datetime


class Service(BaseModel):
    name: str
    type_service: str
    unit: str
    price: float


class Image(BaseModel):
    url: HttpUrl
    name: str


class Apartment(BaseModel):
    number: int
    floor: int
    entrance: int
    square_apart: float
    #  house: House


class House(BaseModel):
    street: str
    number: int
    square: float
    number_storeys: int
    number_entrances: int
    year_constraction: date
    image: list[Image] | None
    apartments: list[Apartment]


class resource_counter(BaseModel):
    serial_number: str
    type_counter: str
    type_resource: str
    install_location: str
    commissioning_date: date
    verification_date: date
    next_verification_date: date
    meter_reading: list[int] | None
