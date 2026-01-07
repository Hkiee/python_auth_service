from datetime import datetime
from typing import Sequence

from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.modules.auth.infrastructure.postgres import Base
import sqlalchemy as sa


class UserModel(Base):
    __tablename__ = "users"

    login: Mapped[str] = mapped_column(
        sa.String, unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(sa.String, nullable=False)
    email: Mapped[str] = mapped_column(
        sa.String, unique=True, index=True, nullable=False
    )
    tg_chat_id: Mapped[int] = mapped_column(
        sa.BigInteger, unique=True, index=True, nullable=False
    )
    deleted_at: Mapped[datetime | None] = mapped_column(
        sa.DateTime(timezone=True), nullable=True, default=None
    )
    is_deleted: Mapped[bool] = mapped_column(
        sa.Boolean, server_default=sa.text("false")
    )
    is_active: Mapped[bool] = mapped_column(sa.Boolean, default=True)
