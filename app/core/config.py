"""Application configuration helpers."""

from dataclasses import dataclass
import os

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Runtime settings loaded from environment variables."""

    dashscope_api_key: str
    dashscope_base_url: str
    dashscope_model: str
    openai_api_key: str


def get_settings() -> Settings:
    """Return application settings."""

    return Settings(
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY", "").strip(),
        dashscope_base_url=os.getenv(
            "DASHSCOPE_BASE_URL",
            "https://dashscope.aliyuncs.com/compatible-mode/v1",
        ),
        dashscope_model=os.getenv("DASHSCOPE_MODEL", "qwen-plus"),
        openai_api_key=os.getenv("OPENAI_API_KEY", "").strip(),
    )
