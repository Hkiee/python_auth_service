import logging
from dataclasses import asdict

from sqlalchemy import select, update, func, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.exceptions import NotFoundError
from src.modules.auth.application.interfaces.i_user_repo import IUserRepo
from src.modules.auth.entity.users import UserEntity
from src.modules.auth.infrastructure.postgres.users.orm_model import UserModel
from src.persistence.db.interface import get_async_session


class UsersRepository(IUserRepo):
    def __init__(self, session: get_async_session):
        self.session: AsyncSession = session

    async def get_by_login(
        self, login: str, is_deleted: bool | None = False
    ) -> UserEntity:
        query = select(UserModel).where(UserModel.login == login)
        if is_deleted is not None:
            query = query.where(UserModel.is_deleted == is_deleted)
        res = await self.session.execute(query)
        obj = res.scalar_one_or_none()
        if not obj:
            raise NotFoundError
        return obj.to_entity()