from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .mixin import UserRelationMixin

from .base import Base


class New(UserRelationMixin, Base):
    _user_back_populates = "news"
    title: Mapped[str] = mapped_column(String(100), unique=False)
    text: Mapped[str] = mapped_column(Text, default="", server_default="")
    created_date: Mapped[str]

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, user_id={self.user_id})"
        )

    def __repr__(self):
        return str(self)
