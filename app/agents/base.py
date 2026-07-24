"""Base agent abstraction for CareerPilot AI."""

from app.core.llm import LLMClient


class BaseAgent:
    """Shared foundation for future CareerPilot AI agents."""

    def __init__(
        self,
        name: str,
        description: str,
        llm_client: LLMClient | None = None,
    ) -> None:
        """Create an agent with identity details and an LLM dependency."""

        # An Agent is a focused AI worker that will eventually own one kind of
        # career task, such as resume review, interview practice, or learning
        # guidance. For now, this base class keeps the first agent concept very
        # small and easy to understand.
        self.name = name
        self.description = description

        # All future agents should inherit from BaseAgent so they start with the
        # same simple interface and shared setup. That keeps agent code
        # consistent as the project grows instead of each agent inventing its
        # own constructor or run method.
        self._llm_client = llm_client or LLMClient()

    def run(self, task: str) -> str:
        """Run a task through the shared LLM client and return its response."""

        # Agents depend on LLMClient instead of calling OpenAI, Anthropic, or
        # other providers directly. This keeps provider details, API keys, and
        # model-switching logic in one core abstraction rather than spreading
        # those decisions across every agent implementation.
        return self._llm_client.chat(task)
