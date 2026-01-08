from dishka import AsyncContainer, make_async_container

from src.di.persistence.db import DBProvider
from src.di.auth.services import AuthServiceProvider
from src.di.auth.usecases import AuthProcessProvider
from src.di.auth.repositories import AuthRepoProvider



def get_async_container() -> AsyncContainer:
    #persistence
    db_provider = DBProvider()

    #auth module
    auth_service_provider = AuthServiceProvider()
    auth_process_provider = AuthProcessProvider()
    auth_repo_provider = AuthRepoProvider()

    return make_async_container(
        db_provider,
        auth_service_provider,
        auth_process_provider,
        auth_repo_provider
    )