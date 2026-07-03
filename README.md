# CareerPilot AI

CareerPilot AI is a planned production-quality, agentic AI career assistant. The project is starting with a clean Python foundation that can evolve into a modular system for multi-agent collaboration, career guidance workflows, long-term memory, retrieval-augmented generation, observability, and evaluation.

This repository currently contains only the initial project skeleton. Business logic, API endpoints, user interfaces, agents, RAG, memory, and tool-calling features are not implemented yet.

## Planned Architecture

The intended architecture will separate application concerns into focused modules:

- **Application entry point** for starting the project in future runtime environments.
- **Core infrastructure** for configuration and logging shared across the application.
- **Agent modules** for future planning, resume, interview, career advisor, and learning agents.
- **API layer** for a future FastAPI backend.
- **Memory layer** for future long-term and session memory capabilities.
- **Model layer** for future domain and data schemas.
- **Prompt layer** for future prompt templates and prompt management.
- **RAG layer** for future retrieval and knowledge workflows.
- **Tool layer** for future tool-calling integrations.
- **Documentation and tests** to support maintainability as the system grows.

## Folder Explanation

```text
app/
  agents/    Future AI agent modules.
  api/       Future backend API modules.
  core/      Shared configuration and logging utilities.
  memory/    Future memory components.
  models/    Future application schemas and data models.
  prompts/   Future prompt templates and prompt utilities.
  rag/       Future retrieval-augmented generation components.
  tools/     Future tool-calling integrations.
docs/        Project documentation.
tests/       Automated tests.
main.py      Application entry point placeholder.
```

## Development Roadmap

1. Establish the Python project skeleton, configuration template, logging utility, and documentation.
2. Add baseline development tooling and automated tests.
3. Introduce the FastAPI backend structure.
4. Add initial agent interfaces and orchestration boundaries.
5. Implement memory and RAG foundations.
6. Add tool-calling integrations and MCP support.
7. Add observability, evaluation workflows, and deployment assets.
8. Iterate toward production-ready application features.
