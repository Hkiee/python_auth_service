from dishka import Provider, provide, Scope

from src.modules.auth.application.interfaces.i_user_repo import IUserRepo
from src.modules.auth.infrastructure.postgres.users.repository import UsersRepository


class AuthRepoProvider(Provider):
    user_repo_provider = provide(
        source=UsersRepository, provides=IUserRepo, scope=Scope.REQUEST
    )
