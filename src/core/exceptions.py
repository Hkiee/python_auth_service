from fastapi import HTTPException


class AuthorizationError(HTTPException):
    raise HTTPException(status_code=401)

class NotFoundError(HTTPException):
    raise HTTPException(status_code=404)