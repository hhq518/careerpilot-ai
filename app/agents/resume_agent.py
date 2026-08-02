from app.agents.base import BaseAgent
from app.prompts import RESUME_AGENT_PROMPT


class ResumeAgent(BaseAgent):
    """
    Agent specialized in resume optimization.
    """

    def __init__(self):
        super().__init__(
            name="resume_agent",
            description="AI resume optimization specialist",
            system_prompt=RESUME_AGENT_PROMPT,
        )