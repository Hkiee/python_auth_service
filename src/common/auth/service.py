from abc import ABC, abstractmethod

from fastapi.security import HTTPAuthorizationCredentials

from src.modules.auth.entity.users import UserEntity


class IAuthService(ABC):
    @abstractmethod
    async def jwt_auth(
        self, credentials: HTTPAuthorizationCredentials
    ) -> UserEntity: ...

    @abstractmethod
    async def get_by_login(self, login: str) -> UserEntity: ...

    @abstractmethod
    async def delete(self, id_: int) -> None: ...
