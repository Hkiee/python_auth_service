import uuid
import sqlalchemy as sa

from uuid_extensions import uuid7
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped

from modules.auth.entity.users import UserEntity
from src.modules.auth.infrastructure.postgres import Base
from sqlalchemy.dialects.postgresql import UUID


class UserModel(Base):
    __tablename__ = "users"

    user_uuid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid7
    )

    login: Mapped[str] = mapped_column(
        sa.String, unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(sa.String, nullable=False)
    email: Mapped[str] = mapped_column(
        sa.String, unique=True, index=True, nullable=False
    )
    deleted_at: Mapped[datetime | None] = mapped_column(
        sa.DateTime(timezone=True), nullable=True, default=None
    )
    is_deleted: Mapped[bool] = mapped_column(
        sa.Boolean, server_default=sa.text("false")
    )
    is_active: Mapped[bool] = mapped_column(sa.Boolean, default=True)

    def to_entity(self):
        return UserEntity(
            id=self.id,
            login=self.login,
            hashed_password=self.hashed_password,
            deleted_at=self.deleted_at,
            is_deleted=self.is_deleted,
            is_active=self.is_active,
            email=self.email,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            user_uuid=self.user_uuid,
        )
