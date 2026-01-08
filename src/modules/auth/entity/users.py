from dataclasses import dataclass
from uuid import UUID
from typing import Optional
from datetime import datetime


@dataclass
class UserEntity:
    id: int
    user_uuid: UUID
    hashed_password: str
    login: str
    email: str
    is_deleted: bool
    is_active: bool

    deleted_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
