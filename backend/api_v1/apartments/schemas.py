from pydantic import BaseModel, ConfigDict


class ApartmentBase(BaseModel):
    number: int
    floor: int
    entrance: int
    square_apart: float
    house_id: int


class Apartment(ApartmentBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ApartmentCreate(ApartmentBase):
    pass


class ApartmentUpdate(ApartmentCreate):
    pass


class ApartmentUpdatePartial(ApartmentCreate):
    number: int | None = None
    floor: int | None = None
    entrance: int | None = None
    square_apart: float | None = None
