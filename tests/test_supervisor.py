from app.agents import AgentRegistry
from app.agents.supervisor_agent import SupervisorAgent


def test_supervisor_handle():

    registry = AgentRegistry()

    supervisor = SupervisorAgent(
        registry
    )

    result = supervisor.handle(
        "帮我优化AI岗位简历"
    )

    print(result)


if __name__ == "__main__":
    test_supervisor_handle()