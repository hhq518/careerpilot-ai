from app.agents.base import BaseAgent
from app.core.llm import LLMClient
from app.prompts import CAREER_AGENT_PROMPT


class CareerAgent(BaseAgent):
    """
    Agent specialized in career planning.
    """

    def __init__(self, llm_client: LLMClient | None = None) -> None:
        super().__init__(
            name="career_agent",
            description="AI career planning specialist",
            system_prompt=CAREER_AGENT_PROMPT,
            llm_client=llm_client,
        )