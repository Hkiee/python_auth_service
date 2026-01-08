from dishka import Provider, provide, Scope

from src.common.auth.service import IAuthService
from src.modules.auth.infrastructure.services.auth import AuthServiceImpl


class AuthServiceProvider(Provider):
    auth_provider = provide(
        source=AuthServiceImpl, provides=IAuthService, scope=Scope.REQUEST
    )
