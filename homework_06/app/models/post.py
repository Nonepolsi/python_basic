from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from .flask_db import db
from .int_id_pk_mixin import IntIdPkMixin

if TYPE_CHECKING:
    from models import User



class Post(IntIdPkMixin, db.Model):
    title: Mapped[str] = mapped_column(unique=True)
    body: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="posts")