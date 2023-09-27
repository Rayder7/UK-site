from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    price: float


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class ProductUpdatePartial(ProductCreate):
    name: str | None = None
    price: float | None = None
