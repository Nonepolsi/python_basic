from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .flask_db import db
from .int_id_pk_mixin import IntIdPkMixin

if TYPE_CHECKING:
    from models import Post



class User(IntIdPkMixin, db.Model):
    name: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user")