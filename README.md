# CareerPilot AI

CareerPilot AI is a planned production-quality, agentic AI career assistant. The project is starting with a clean Python foundation that can evolve into a modular system for multi-agent collaboration, career guidance workflows, long-term memory, retrieval-augmented generation, observability, and evaluation.

This repository now includes a minimal FastAPI backend bootstrap with beginner-friendly health, configuration-check, and chat endpoints. User interfaces, agents, RAG, memory, real LLM provider calls, and tool-calling features are not implemented yet. A minimal provider-independent LLM Client layer and service layer are available so future agents have safe boundaries for model access and business logic.

## Local Development

Install dependencies, then start the local FastAPI server with:

```bash
uvicorn main:app --reload
```

After the server starts, visit `http://127.0.0.1:8000/` for the health check, `http://127.0.0.1:8000/config-check` for a safe configuration import check, or `http://127.0.0.1:8000/docs` for the FastAPI Swagger UI. The docs page also shows the minimal `POST /chat` endpoint.

## Chat Endpoint

`POST /chat` accepts a JSON body with a `message` field. The route calls `ChatService`, which validates the message and then uses the placeholder `LLMClient.chat()` method. It does not call a real LLM provider yet, and it does not implement agents, RAG, or memory.

Example request:

```json
{
  "message": "Help me plan my next career move."
}
```

Example response:

```json
{
  "input": "Help me plan my next career move.",
  "response": "LLM provider integration is not configured yet. A real model response will be added in a future implementation.",
  "provider_status": "placeholder",
  "service": "chat_service"
}
```

Empty or whitespace-only messages return a safe validation error instead of reaching the LLM client.

## Planned Architecture

The intended architecture will separate application concerns into focused modules:

- **Application entry point** for creating the FastAPI application.
- **Core infrastructure** for configuration, logging, and the provider-independent LLM Client shared across the application.
- **Service layer** for business logic between API routes and the LLM client, agents, memory, or RAG.
- **Agent modules** for future planning, resume, interview, career advisor, and learning agents.
- **API layer** for minimal FastAPI routes and future backend modules.
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
  api/       FastAPI route modules.
  core/      Shared configuration, logging, and LLM client utilities.
  memory/    Future memory components.
  services/  Business logic between API routes and core/future agent modules.
  models/    Future application schemas and data models.
  prompts/   Future prompt templates and prompt utilities.
  rag/       Future retrieval-augmented generation components.
  tools/     Future tool-calling integrations.
docs/        Project documentation.
tests/       Automated tests.
main.py      FastAPI application entry point.
```

## Development Roadmap

1. Establish the Python project skeleton, configuration template, logging utility, and documentation.
2. Add baseline development tooling and automated tests.
3. Introduce the FastAPI backend structure.
4. Extend the LLM Client with real provider integrations while keeping secrets isolated.
5. Add initial agent interfaces and orchestration boundaries.
6. Implement memory and RAG foundations.
7. Add tool-calling integrations and MCP support.
8. Add observability, evaluation workflows, and deployment assets.
9. Iterate toward production-ready application features.
