from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column
from annotated_types import MaxLen, MinLen
from uuid import UUID
from pydantic import EmailStr
from datetime import date
from fastapi import Body, Query
from .base import Base


class User(Base):
    email: Mapped[str] = mapped_column(unique=True)
