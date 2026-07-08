"""API routes for the CareerPilot AI backend."""

from fastapi import APIRouter

from app.core.config import get_settings


router = APIRouter()


@router.get("/")
def read_root() -> dict[str, str]:
    """Return a basic project status message."""

    return {
        "project": "CareerPilot AI",
        "status": "FastAPI backend is running",
    }


@router.get("/config-check")
def config_check() -> dict[str, bool | str]:
    """Confirm configuration can load without returning secret values."""

    get_settings()
    return {
        "config_loaded": True,
        "secrets_exposed": False,
        "message": "Configuration loaded safely.",
    }
