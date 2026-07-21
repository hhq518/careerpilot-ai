"""Provider-independent LLM client abstraction for CareerPilot AI."""

from app.core.config import Settings, get_settings


class LLMClient:
    """Small boundary between CareerPilot agents and future model providers."""

    def __init__(self, settings: Settings | None = None) -> None:
        """Create an LLM client using application settings."""

        self._settings = settings or get_settings()

    def chat(self, message: str) -> str:
        """Return a placeholder chat response until provider integration is added."""

        # LLMClient exists so the rest of the app has one simple place to ask
        # for language-model responses instead of depending on vendor SDKs.
        # Future agents should call this abstraction, not model providers
        # directly, so provider details and secrets stay isolated in core code.
        # Keeping this boundary small will make it easier to switch models or
        # add providers later without rewriting agent, RAG, or workflow logic.
        _ = message
        _ = self._settings
        return (
            "LLM provider integration is not configured yet. "
            "A real model response will be added in a future implementation."
        )
