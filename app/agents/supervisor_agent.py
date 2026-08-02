"""Supervisor agent for routing user requests."""


class SupervisorAgent:
    """
    Decide which agent should handle a user task.

    This is the first simple version.
    Later it can be upgraded with LLM-based routing.
    """

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