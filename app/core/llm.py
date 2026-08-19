"""Provider-independent LLM client abstraction for CareerPilot AI."""

from openai import OpenAI

from app.core.config import Settings, get_settings


class LLMClient:
    """Small boundary between CareerPilot agents and model providers."""

    def __init__(self, settings: Settings | None = None) -> None:
        """Create an LLM client using application settings."""

        self._settings = settings or get_settings()

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