from pydantic import BaseModel, ConfigDict


class Product(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    price: float


class ProductCreate(BaseModel):
    pass
