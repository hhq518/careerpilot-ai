"""Provider-independent LLM client abstraction for CareerPilot AI."""

from openai import OpenAI

from app.core.config import Settings, get_settings


class LLMClient:
    """Small boundary between CareerPilot agents and model providers.

    Provider-specific code lives here so agents only need to know how to ask
    for a response. This prevents API keys, vendor URLs, and SDK details from
    leaking into every specialized agent and makes a future provider change a
    small, centralized update.
    """

    def __init__(self, settings: Settings | None = None) -> None:
        """Create an LLM client using application settings."""

        self._settings = settings or get_settings()

    @property
    def provider_status(self) -> str:
        """Return a safe status label without exposing provider credentials."""

        if self._settings.dashscope_api_key:
            return "configured"
        return "not_configured"

    def chat(self, message: str) -> str:
        """
        Send a message to the configured LLM provider.

        For now, CareerPilot AI uses DashScope/Qwen through
        an OpenAI-compatible API.
        """

        if not self._settings.dashscope_api_key:
            return (
                "LLM provider integration is not configured yet. "
                "Please set DASHSCOPE_API_KEY in your .env file."
            )

        # DashScope supports the OpenAI client protocol. Keeping this setup in
        # LLMClient means neither ChatService nor an agent directly depends on
        # DashScope/OpenAI-compatible request details.
        client = OpenAI(
            api_key=self._settings.dashscope_api_key,
            base_url=self._settings.dashscope_base_url,
        )

        response = client.chat.completions.create(
            model=self._settings.dashscope_model,
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content

        if not content:
            return "The model returned an empty response."

        return content
