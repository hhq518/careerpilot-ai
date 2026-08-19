"""Focused tests for runtime memory and chat orchestration."""

from app.core.config import Settings
from app.core.llm import LLMClient
from app.memory.memory_manager import MemoryManager
from app.services.chat_service import ChatService


class RecordingLLMClient:
    """Test double that records the prompt sent by ChatService."""

    def __init__(self) -> None:
        self.last_message = ""
        self.provider_status = "configured"

    def chat(self, message: str) -> str:
        self.last_message = message
        return "test response"


def test_users_have_separate_memory_records() -> None:
    manager = MemoryManager()
    manager.save_memory("alice", "Interested in machine learning")
    manager.save_memory("bob", "Preparing for backend interviews")

    assert manager.get_memory("alice") == ["Interested in machine learning"]
    assert manager.get_memory("bob") == ["Preparing for backend interviews"]


def test_chat_service_accepts_user_id_and_enriches_prompt() -> None:
    manager = MemoryManager()
    manager.save_memory("alice", "Interested in machine learning")
    llm_client = RecordingLLMClient()
    service = ChatService(llm_client=llm_client, memory_manager=manager)

    result = service.handle_message("alice", "Plan my next career step")

    assert "Interested in machine learning" in llm_client.last_message
    assert "Plan my next career step" in llm_client.last_message
    assert result["input"] == "Plan my next career step"
    assert result == {
        "input": "Plan my next career step",
        "response": "test response",
        "provider_status": "configured",
        "service": "chat_service",
    }


def test_llm_client_returns_fallback_without_dashscope_key() -> None:
    settings = Settings(
        dashscope_api_key="",
        dashscope_base_url="https://example.invalid/v1",
        dashscope_model="qwen-plus",
        openai_api_key="unused-openai-key",
    )
    client = LLMClient(settings=settings)

    assert client.chat("Hello") == (
        "LLM provider integration is not configured yet. "
        "Please set DASHSCOPE_API_KEY in your .env file."
    )
    assert client.provider_status == "not_configured"


def test_chat_service_reports_provider_is_not_configured() -> None:
    client = LLMClient(
        settings=Settings(
            dashscope_api_key="",
            dashscope_base_url="https://example.invalid/v1",
            dashscope_model="qwen-plus",
            openai_api_key="",
        )
    )

    result = ChatService(llm_client=client).handle_message("alice", "Career plan")

    assert set(result) == {"input", "response", "provider_status", "service"}
    assert result["provider_status"] == "not_configured"
