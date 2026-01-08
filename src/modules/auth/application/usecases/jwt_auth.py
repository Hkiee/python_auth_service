from fastapi.security import HTTPAuthorizationCredentials
import jwt

from src.core.config import config
from src.core.exceptions import AuthorizationError
from src.modules.auth.application.interfaces.i_user_repo import IUserRepo
from src.modules.auth.entity.users import UserEntity


class JwtAuthUseCase:
    def __init__(self, user_repo: IUserRepo):
        self.user_repo = user_repo

    async def execute(self, credentials: HTTPAuthorizationCredentials) -> UserEntity:
        try:
            token = credentials.credentials
            payload = jwt.decode(
                token, config.jwt.secret, algorithms=[config.jwt.algorithm]
            )
            login = payload.get("sub")
            if not login:
                raise AuthorizationError
            return await self.user_repo.get_by_login(login)
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            raise AuthorizationError
