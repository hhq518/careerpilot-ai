# CareerPilot AI

CareerPilot AI is a planned production-quality, agentic AI career assistant. The project is starting with a clean Python foundation that can evolve into a modular system for multi-agent collaboration, career guidance workflows, long-term memory, retrieval-augmented generation, observability, and evaluation.

This repository now includes a minimal FastAPI backend bootstrap with beginner-friendly health, configuration-check, and chat endpoints. User interfaces, specialized agents, RAG, persistent memory, real LLM provider calls, and tool-calling features are not implemented yet. A minimal provider-independent LLM Client layer, service layer, runtime memory component, Agent base layer, and prompt management layer are available so future agents have safe boundaries for model access, business logic, and role-specific instructions.

## Local Development

Install dependencies, then start the local FastAPI server with:

```bash
uvicorn main:app --reload
```

After the server starts, visit `http://127.0.0.1:8000/` for the health check, `http://127.0.0.1:8000/config-check` for a safe configuration import check, or `http://127.0.0.1:8000/docs` for the FastAPI Swagger UI. The docs page also shows the minimal `POST /chat` endpoint.

## Chat Endpoint

`POST /chat` accepts a JSON body with `user_id` and `message` fields. The `user_id` identifies which user's memory should be retrieved; it is not an authentication mechanism. The route calls `ChatService`, which validates the message, retrieves that user's runtime memory, combines the memory context with the current task, and sends the enriched prompt to the placeholder `LLMClient.chat()` method. It does not call a real LLM provider yet, and it does not implement specialized agents or RAG.

Example request:

```json
{
  "user_id": "hhq518",
  "message": "help me plan my AI career"
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

## Current Memory Flow

The current chat flow keeps each layer focused on one responsibility:

```text
POST /chat request
    ↓
ChatService validates the message
    ↓
MemoryManager looks up records by user_id
    ↓
ChatService combines memory with the current user task
    ↓
LLMClient.chat() receives the enriched prompt
```

`ChatService` coordinates the lookup and model call because they are business workflow concerns, while `MemoryManager` stays independent from Agent logic and provider code. This separation will allow the memory implementation to change without redesigning agents.

Memory is currently stored only in the running application's process. It is cleared whenever the process restarts and is not shared between multiple server processes. A future version may replace this runtime-only implementation with database or other persistent storage; the current version intentionally does not provide persistence.

## Planned Architecture

The intended architecture will separate application concerns into focused modules:

- **Application entry point** for creating the FastAPI application.
- **Core infrastructure** for configuration, logging, and the provider-independent LLM Client shared across the application.
- **Service layer** for business logic between API routes and the LLM client, agents, memory, or RAG.
- **Agent modules** with a shared `BaseAgent` foundation for future planning, resume, interview, career advisor, and learning agents.
- **API layer** for minimal FastAPI routes and future backend modules.
- **Memory layer** for current per-user runtime records and future persistent memory capabilities.
- **Model layer** for future domain and data schemas.
- **Prompt layer** for future prompt templates and prompt management.
- **RAG layer** for future retrieval and knowledge workflows.
- **Tool layer** for future tool-calling integrations.
- **Documentation and tests** to support maintainability as the system grows.

## Agent Role System

The first Agent abstraction lives in `app/agents/base.py`. `BaseAgent` gives future agents a shared name, description, `system_prompt`, `LLMClient` dependency, and `run(task: str) -> str` method. The `system_prompt` is the role instruction that tells the model how a specific agent should behave before it handles the user's task.

When `run()` is called, `BaseAgent` combines the agent's system prompt with the user task and sends that final prompt to `LLMClient.chat()`. This keeps the implementation intentionally small: it does not introduce LangChain, LangGraph, memory, RAG, tools, function calling, or multi-agent collaboration.

Future CareerPilot agents can inherit from `BaseAgent` when they need a consistent interface for focused workflows, such as resume feedback, interview coaching, career planning, or learning path guidance. Keeping agents dependent on `LLMClient` instead of provider SDKs directly will make it easier to add real model providers later while keeping API keys and vendor-specific logic isolated in the core layer.

## Prompt Management

Prompt templates live in `app/prompts/agent_prompts.py` instead of being hard-coded inside agent classes. Separating prompts from agent logic makes the code easier to maintain because role instructions can be reviewed, edited, and versioned without changing the Python workflow that runs an agent.

The current prompt module defines three starter system prompts:

- `RESUME_AGENT_PROMPT` for resume and CV improvement.
- `INTERVIEW_AGENT_PROMPT` for interview preparation and coaching.
- `CAREER_AGENT_PROMPT` for career direction, job search strategy, and growth planning.

Each prompt defines the agent's role, responsibilities, and behavior rules. Different agents need different system prompts because a resume reviewer, interview coach, and career advisor should guide the same user in different ways. This structure also prepares the project for future multi-agent expansion without implementing multi-agent collaboration yet.

## Folder Explanation

```text
app/
  agents/    Shared BaseAgent abstraction and future AI agent modules.
  api/       FastAPI route modules.
  core/      Shared configuration, logging, and LLM client utilities.
  memory/    Per-user runtime memory and future persistent memory components.
  services/  Business logic between API routes and core/future agent modules.
  models/    Future application schemas and data models.
  prompts/   Agent system prompt templates and future prompt utilities.
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
5. Expand from the initial BaseAgent interface into focused agent workflows and orchestration boundaries.
6. Implement memory and RAG foundations.
7. Add tool-calling integrations and MCP support.
8. Add observability, evaluation workflows, and deployment assets.
9. Iterate toward production-ready application features.
