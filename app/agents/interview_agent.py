from app.agents.base import BaseAgent
from app.prompts import INTERVIEW_AGENT_PROMPT


class InterviewAgent(BaseAgent):
    """
    Agent specialized in AI interview simulation.
    """

    def __init__(self):
        super().__init__(
            name="interview_agent",
            description="AI interview simulation specialist",
            system_prompt=INTERVIEW_AGENT_PROMPT,
        )