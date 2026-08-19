"""Chat service for coordinating memory and the agent pipeline."""

from app.core.llm import LLMClient
from app.memory.memory_manager import MemoryManager
from app.agents.supervisor_agent import SupervisorAgent
from app.agents import AgentRegistry


class ChatService:
    """Handle chat business flow between API routes and the agent pipeline."""

    def __init__(
        self,
        llm_client: LLMClient | None = None,
        memory_manager: MemoryManager | None = None,
        supervisor: SupervisorAgent | None = None,
    ) -> None:
        """Create the service with its LLM and memory dependencies."""

        self._llm_client = llm_client or LLMClient()
        self._memory_manager = memory_manager or MemoryManager()
        self._supervisor = supervisor or SupervisorAgent(
            AgentRegistry(llm_client=self._llm_client)
        )

    def handle_message(self, user_id: str, message: str) -> dict[str, str]:
        """Validate a user message and return the agent pipeline response."""

        # The service layer exists so routes stay focused on HTTP details such
        # as request bodies, response formats, and status codes.
        # Business logic belongs here instead of directly in route functions so
        # it can be reused later by other entry points, tests, background jobs,
        # or future user interfaces without copying FastAPI-specific code.
        cleaned_message = message.strip()
        if not cleaned_message:
            raise ValueError("Message must not be empty.")

        # A user_id is the lookup key that prevents one person's memories from
        # being included in another person's prompt.
        memories = self._memory_manager.get_memory(user_id)
        memory_context = "\n".join(f"- {memory}" for memory in memories)
        if not memory_context:
            memory_context = "No saved memory for this user."

        enriched_prompt = (
            "Relevant user memory:\n"
            f"{memory_context}\n\n"
            "Current user task:\n"
            f"{cleaned_message}"
        )

        # ChatService coordinates memory lookup and the LLM call because this
        # is application workflow, while the route handles only HTTP concerns.
        response = self._supervisor.handle(enriched_prompt)

        # MemoryManager stays separate from Agent logic so storage can later
        # change without coupling agents to an in-memory or database backend.
        return {
            "input": cleaned_message,
            "response": response,
            "provider_status": self._llm_client.provider_status,
            "service": "chat_service",
        }
