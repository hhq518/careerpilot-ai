"""Chat service for coordinating chat requests before agents exist."""

from app.core.llm import LLMClient


class ChatService:
    """Handle chat-related business flow between API routes and the LLM client."""

    def __init__(self, llm_client: LLMClient | None = None) -> None:
        """Create the service with an LLM client dependency."""

        self._llm_client = llm_client or LLMClient()

    def handle_message(self, message: str) -> dict[str, str]:
        """Validate a user message and return the placeholder LLM response."""

        # The service layer exists so routes stay focused on HTTP details such
        # as request bodies, response formats, and status codes.
        # Business logic belongs here instead of directly in route functions so
        # it can be reused later by other entry points, tests, background jobs,
        # or future user interfaces without copying FastAPI-specific code.
        cleaned_message = message.strip()
        if not cleaned_message:
            raise ValueError("Message must not be empty.")

        response = self._llm_client.chat(cleaned_message)

        # Later, ChatService can become the first stop for Agent orchestration:
        # it can choose a career-planning agent, pass the message into that
        # agent, and still keep the API route small and easy to understand.
        return {
            "input": cleaned_message,
            "response": response,
            "provider_status": "placeholder",
            "service": "chat_service",
        }
