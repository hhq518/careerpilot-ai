from app.agents.supervisor_agent import SupervisorAgent


def test_supervisor():

    supervisor = SupervisorAgent()

    print(
        supervisor.decide(
            "帮我优化AI岗位简历"
        )
    )

    print(
        supervisor.decide(
            "帮我模拟大模型应用开发面试"
        )
    )

    print(
        supervisor.decide(
            "帮我规划AI职业路线"
        )
    )


if __name__ == "__main__":
    test_supervisor()