from typing import Annotated
from annotated_types import MaxLen, MinLen
from uuid import UUID
from pydantic import BaseModel, EmailStr
from datetime import date
from fastapi import Body, Query

""" 
class WorkingPosition(BaseModel):
    id: id
    name: str
    department: str


class UserRole(BaseModel):
    id: id
    name: str
    permission: str """


class CreateUser(BaseModel):
    id: UUID
    email: EmailStr
    password: Annotated[str, MinLen(3), MaxLen(40)]
    phone_number: Annotated[
        int | None,
        Query(
            pattern="^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
        ),
    ]
    first_name: Annotated[str, MinLen(3), MaxLen(20)]
    last_name: Annotated[str, MinLen(3), MaxLen(20)]
    middle_name: Annotated[str, MinLen(3), MaxLen(20)]
    date_of_birth: date | None = Body(default=None)
    residential_addres: Annotated[str, MinLen(3), MaxLen(25)]
    #user_role: UserRole
    #working_position: WorkingPosition | None
