"""FastAPI application entry point for CareerPilot AI."""

from fastapi import FastAPI

from app.api.routes import router
from app.core.logging import configure_logging


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    configure_logging()

    app = FastAPI(
        title="CareerPilot AI",
        description="Minimal FastAPI backend bootstrap for CareerPilot AI.",
        version="0.1.0",
    )
    app.include_router(router)
    return app


app = create_app()
