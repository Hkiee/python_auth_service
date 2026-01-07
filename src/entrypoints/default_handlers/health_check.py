import logging

from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Request


logger = logging.getLogger(__name__)
router = APIRouter(route_class=DishkaRoute)


@router.get("/healthcheck")
async def healthcheck(_: Request):
    return {"status": "pong"}
