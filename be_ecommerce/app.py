"""Main App Logic."""

import secrets

from be_ecommerce.api.routers import router

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    # this service is not exposed so the communication is internal. the basic Auth is only added for the compatiility with other public services
    correct_username = secrets.compare_digest(credentials.username, "aeC0ohph")
    correct_password = secrets.compare_digest(credentials.password, "Zohshu3N")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


def create_app() -> FastAPI:
    """Creates the application."""

    this_app = FastAPI(  
        title="be-commerce: ",
    )

    this_app.include_router(
        router,
    )

    return this_app


app = create_app()
