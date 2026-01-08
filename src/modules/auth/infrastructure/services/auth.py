import logging
from typing import Optional

from fastapi.security import HTTPAuthorizationCredentials

from src.common.auth.service import IAuthService
from src.modules.auth.application.interfaces.i_user_repo import IUserRepo
from src.modules.auth.application.usecases.jwt_auth import JwtAuthUseCase
from src.modules.auth.entity.user import UserEntity

logger = logging.getLogger(__name__)


class AuthServiceImpl(IAuthService):
    def __init__(
        self, jwt_auth_uc: JwtAuthUseCase, repo: IUserRepo
    ):
        self.jwt_auth_uc = jwt_auth_uc
        self.repo = repo


    async def jwt_auth(self, credentials: HTTPAuthorizationCredentials):
        user = await self.jwt_auth_uc.execute(credentials)
        logger.debug(
            "Successfully get user by jwt",
            extra={"extra": {"user": user}},
        )
        return user

    async def get_by_login(self, login: str) -> UserEntity:
        return await self.repo.get_by_login(login)

    async def delete(self, id_: int) -> None:
        return await self.repo.delete(id_)
