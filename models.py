import datetime
from uuid import UUID
from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
# from litestar.plugins.sqlalchemy.base import UUIDAuditBase, UUIDBase
from litestar.plugins.sqlalchemy import base


class UserModel(base.UUIDBase):
    __tablename__ = "user"
    id: Mapped[UUID]
    name: Mapped[str]
    surname: Mapped[str]
    password: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=datetime.datetime.now)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=datetime.datetime.now, onupdate=func.utcnow())
