from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user import User
    from .house import House


class UserRelationMixin:
    _user_id_nullable: bool = False
    _user_id_unique: bool = False
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("users.id"),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable,
        )

    @declared_attr
    def user(cls) -> Mapped["User"]:
        return relationship(
            "User",
            back_populates=cls._user_back_populates,
        )


class HouseRelationMixin:
    _house_id_unique: bool = False
    _house_id_nullable: bool = False
    _house_back_populates: str | None = None

    @declared_attr
    def house_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("houses.id"),
            unique=cls._house_id_unique,
            nullable=cls._house_id_nullable,
        )

    @declared_attr
    def house(cls) -> Mapped["House"]:
        return relationship(
            "House",
            back_populates=cls._house_back_populates,
        )
