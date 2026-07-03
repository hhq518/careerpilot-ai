"""Application configuration helpers."""

from dataclasses import dataclass
import os

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Runtime settings loaded from environment variables."""

    dashscope_api_key: str = os.getenv("DASHSCOPE_API_KEY", "")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")


def get_settings() -> Settings:
    """Return application settings."""

    return Settings()
