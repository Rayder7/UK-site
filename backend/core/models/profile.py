from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .mixin import UserRelationMixin

from .base import Base


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"

    personal_account: Mapped[int] = mapped_column(unique=True)
    phone_number: Mapped[int] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str] = mapped_column(String(25), unique=False)
    last_name: Mapped[str] = mapped_column(String(25), unique=False)
    middle_name: Mapped[str] = mapped_column(String(25), unique=False)
    date_of_birth: Mapped[str] = mapped_column(String(25), unique=False)
    residential_addres: Mapped[str] = mapped_column(String(30), unique=False)
