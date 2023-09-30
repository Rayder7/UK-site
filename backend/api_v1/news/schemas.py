from fastapi import Header
from pydantic import BaseModel, ConfigDict, validator
from datetime import datetime


class NewsBase(BaseModel):
    title: str
    text: str
    created_date: datetime
    user_id: int


class News(NewsBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class NewsCreate(BaseModel):
    title: str
    text: str


class NewsUpdate(NewsCreate):
    pass


class NewsUpdatePartial(NewsCreate):
    title: str | None = None
    text: str | None = None
