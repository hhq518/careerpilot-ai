from app.agents.registry import AgentRegistry


class SupervisorAgent:
    """
    Supervisor responsible for routing tasks
    to specialized agents.
    """

    def __init__(self, registry):
        self.registry = registry

    def decide(self, message: str) -> str:
        """
        Return the target agent name.
        """
        message = message.lower()

        if "简历" in message or "resume" in message:
            return "resume"

        if "面试" in message or "interview" in message:
            return "interview"

        if "职业" in message or "规划" in message:
            return "career"

        return "career"

    def handle(self, message: str) -> str:
        """
        Route message and execute selected agent.
        """
        agent_name = self.decide(message)
        agent = self.registry.get_agent(agent_name)
        return agent.run(message)