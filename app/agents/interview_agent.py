from app.agents.base import BaseAgent
from app.core.llm import LLMClient
from app.prompts import INTERVIEW_AGENT_PROMPT


class InterviewAgent(BaseAgent):
    """
    Agent specialized in AI interview simulation.
    """

    def __init__(self, llm_client: LLMClient | None = None) -> None:
        super().__init__(
            name="interview_agent",
            description="AI interview simulation specialist",
            system_prompt=INTERVIEW_AGENT_PROMPT,
            llm_client=llm_client,
        )