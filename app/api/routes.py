"""API routes for the CareerPilot AI backend."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.config import get_settings
from app.services.chat_service import ChatService


router = APIRouter()


class ChatRequest(BaseModel):
    """Request body for the minimal chat endpoint."""

    message: str


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


@router.post("/chat")
def chat(request: ChatRequest) -> dict[str, str]:
    """Handle a chat message through the service layer."""

    # Routes should stay thin: they translate HTTP requests into service calls
    # and translate service errors into safe HTTP responses. They should not
    # contain business logic, agent orchestration, memory, RAG, or provider code.
    service = ChatService()
    try:
        return service.handle_message(request.message)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
