from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship, mapped_column
from uuid import UUID

from .base import Base

if TYPE_CHECKING:
    from .new import New
    from .profile import Profile


class User(Base):
    id: Mapped[UUID]
    email: Mapped[str]
    hashed_password: Mapped[str]
    is_active: Mapped[bool]
    is_superuser: Mapped[bool]
    is_verified: Mapped[bool]

    news: Mapped[list["New"]] = relationship(
        back_populates="user"
    )  # связь 1 ко многим
    profile: Mapped["Profile"] = relationship(
        back_populates="user"
    )  # связь 1 ко 1

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}"

    def __repr__(self):
        return str(self)
