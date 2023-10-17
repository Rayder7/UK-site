from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user import User
    from .building import Building


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


class BuildingRelationMixin:
    _building_id_unique: bool = False
    _building_id_nullable: bool = False
    _building_back_populates: str | None = None

    @declared_attr
    def building_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("building.id"),
            unique=cls._building_id_unique,
            nullable=cls._building_id_nullable,
        )

    @declared_attr
    def building(cls) -> Mapped["Building"]:
        return relationship(
            "Building",
            back_populates=cls._building_back_populates,
        )
