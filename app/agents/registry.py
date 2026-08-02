"""Agent registry for managing available agents."""

from app.agents.resume_agent import ResumeAgent
from app.agents.interview_agent import InterviewAgent
from app.agents.career_agent import CareerAgent


class AgentRegistry:
    """
    Store and provide available agents.

    Future router/supervisor agents
    will use this registry to select
    the correct agent.
    """

    def __init__(self):
        self.agents = {
            "resume": ResumeAgent(),
            "interview": InterviewAgent(),
            "career": CareerAgent(),
        }

    def get_agent(self, name: str):
        """
        Return an agent by name.
        """

        return self.agents.get(name)
