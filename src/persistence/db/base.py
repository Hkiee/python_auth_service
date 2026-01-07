from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import sqlalchemy as sa


class Base(DeclarativeBase):

    id: Mapped[int] = mapped_column(
        sa.Integer, primary_key=True, autoincrement=True, index=True, unique=True
    )

    created_at: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True),
        server_default=sa.func.now(),
        onupdate=sa.func.now(),
        nullable=False,
    )
