"""Agent registry for managing available agents."""

from app.agents.career_agent import CareerAgent
from app.agents.interview_agent import InterviewAgent
from app.agents.resume_agent import ResumeAgent
from app.core.llm import LLMClient


class AgentRegistry:
    """
    Store and provide available agents.

    The registry only looks up agents.
    It does not decide which agent to use and does not execute them.
    """

    def __init__(self, llm_client: LLMClient | None = None) -> None:
        shared_llm_client = llm_client or LLMClient()

        self.agents = {
            "resume": ResumeAgent(llm_client=shared_llm_client),
            "interview": InterviewAgent(llm_client=shared_llm_client),
            "career": CareerAgent(llm_client=shared_llm_client),
        }

    def get_agent(self, name: str):
        """
        Return an agent by name.
        """

        agent = self.agents.get(name)

        if not agent:
            raise ValueError(f"Agent {name} not found.")

        return agent

    def list_agent_names(self) -> list[str]:
        """
        Return available agent names.
        """

        return list(self.agents.keys())