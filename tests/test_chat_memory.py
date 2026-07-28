"""Focused tests for runtime memory and chat orchestration."""

from app.memory.memory_manager import MemoryManager
from app.services.chat_service import ChatService


class RecordingLLMClient:
    """Test double that records the prompt sent by ChatService."""

    def __init__(self) -> None:
        self.last_message = ""

    def chat(self, message: str) -> str:
        self.last_message = message
        return "test response"


def test_users_have_separate_memory_records() -> None:
    manager = MemoryManager()
    manager.add_memory("alice", "Interested in machine learning")
    manager.add_memory("bob", "Preparing for backend interviews")

    assert manager.get_memory("alice") == ["Interested in machine learning"]
    assert manager.get_memory("bob") == ["Preparing for backend interviews"]


def test_chat_service_accepts_user_id_and_enriches_prompt() -> None:
    manager = MemoryManager()
    manager.add_memory("alice", "Interested in machine learning")
    llm_client = RecordingLLMClient()
    service = ChatService(llm_client=llm_client, memory_manager=manager)

    result = service.handle_message("alice", "Plan my next career step")

    assert "Interested in machine learning" in llm_client.last_message
    assert "Plan my next career step" in llm_client.last_message
    assert result["input"] == "Plan my next career step"
