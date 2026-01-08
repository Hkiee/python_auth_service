from abc import ABC, abstractmethod
from src.modules.auth.entity.users import UserEntity


class IUserRepo(ABC):

    @abstractmethod
    async def get_by_login(self, login: str) -> UserEntity:
        raise NotImplementedError