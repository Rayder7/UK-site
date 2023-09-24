from typing import Annotated
from annotated_types import MaxLen, MinLen
from uuid import UUID
from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    uuid: UUID
    email: EmailStr
    phone_number: int
    first_name: Annotated[str, MinLen(3), MaxLen(20)]
    last_name: Annotated[str, MinLen(3), MaxLen(20)]
    middle_name: Annotated[str, MinLen(3), MaxLen(20)]
    date_of_birth: str
    residential_addres: Annotated[str, MinLen(3), MaxLen(25)]
