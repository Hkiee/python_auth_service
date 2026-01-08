from dishka import Provider, provide, Scope

from src.modules.auth.application.interfaces.i_user_repo import IUserRepo


class AuthRepoProvider(Provider):
    user_repo_provider = provide(
        source=UsersRepository, provides=IUserRepo, scope=Scope.REQUEST
    )
