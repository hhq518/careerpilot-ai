from app.agents import AgentRegistry


def test_registry():

    registry = AgentRegistry()

    resume_agent = registry.get_agent("resume")

    print(resume_agent.name)
    print(resume_agent.description)


if __name__ == "__main__":
    test_registry()