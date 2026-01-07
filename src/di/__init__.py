from dishka import AsyncContainer, make_async_container

from src.di.persistence.db import DBProvider



def get_async_container() -> AsyncContainer:
    #persistence
    db_provider = DBProvider()
    return make_async_container(
        db_provider,
    )