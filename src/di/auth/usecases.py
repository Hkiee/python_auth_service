from dishka import Provider, provide, Scope

from src.modules.auth.application.usecases.jwt_auth import JwtAuthUseCase


class AuthProcessProvider(Provider):
    jwt_auth_provider = provide(source=JwtAuthUseCase, scope=Scope.REQUEST)
