"""Main App Logic."""

from fastapi import Depends, FastAPI

from be_ecommerce.api.routers import router


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
