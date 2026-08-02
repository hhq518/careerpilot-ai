from app.agents import (
    ResumeAgent,
    InterviewAgent,
    CareerAgent,
)


def test_agents():

    agents = [
        ResumeAgent(),
        InterviewAgent(),
        CareerAgent(),
    ]

    for agent in agents:
        print(agent.name)
        print(agent.description)
        print(agent.system_prompt[:50])
        print("---")


if __name__ == "__main__":
    test_agents()