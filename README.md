# CareerPilot AI

CareerPilot AI is a FastAPI career assistant with runtime user memory, a
supervisor, and specialized resume, interview, and career agents. Model access
is isolated behind one `LLMClient`, which currently integrates DashScope/Qwen
through DashScope's OpenAI-compatible API.

## Local setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Copy the environment template and add your DashScope API key:

```bash
cp .env.example .env
```

```dotenv
DASHSCOPE_API_KEY=your_dashscope_api_key_here
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
DASHSCOPE_MODEL=qwen-plus
OPENAI_API_KEY=your_openai_api_key_here
```

`DASHSCOPE_API_KEY` is required for real Qwen responses. The base URL and model
already have safe defaults, so they only need to be changed when using a
different compatible DashScope endpoint or Qwen model. `OPENAI_API_KEY` is
accepted as configuration for future provider support, but it is not used for
the current DashScope integration.

Never commit `.env`: it contains secrets and is intentionally ignored by Git.
Only commit the placeholder values in `.env.example`. The application does not
return or log API keys.

## Run the API

Start the FastAPI development server from the repository root:

```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/` for the health check,
`http://127.0.0.1:8000/config-check` for a secret-safe configuration check, or
`http://127.0.0.1:8000/docs` for Swagger UI.

## Chat and the multi-agent pipeline

Send a request to `POST /chat` with a user identifier and message:

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H 'Content-Type: application/json' \
  -d '{"user_id":"demo-user","message":"Help me improve my resume"}'
```

Every chat request follows the complete application pipeline; the API and
service do not bypass memory or agent orchestration:

```text
API route
  -> ChatService
  -> MemoryManager (loads this user's runtime context)
  -> SupervisorAgent (selects the appropriate specialist)
  -> AgentRegistry
  -> ResumeAgent / InterviewAgent / CareerAgent
  -> BaseAgent
  -> LLMClient
  -> DashScope/Qwen (when configured)
```

The response schema remains stable:

```json
{
  "input": "Help me improve my resume",
  "response": "...",
  "provider_status": "configured",
  "service": "chat_service"
}
```

`provider_status` is `configured` when `DASHSCOPE_API_KEY` is available and
`not_configured` otherwise. Without the key, the same full memory and agent
pipeline runs, but `LLMClient` returns a safe setup message instead of making a
network call.

## Architecture boundaries

- `app/api` handles HTTP input and output.
- `app/services` coordinates the chat workflow.
- `app/memory` keeps per-user records in process. Memory is cleared on restart
  and is not persistent or shared across server processes.
- `app/agents` contains supervisor routing, the registry, and focused agents.
- `app/core/llm.py` is the only module that directly calls a model provider.
- `app/prompts` stores role-specific agent instructions.

This iteration intentionally does not add LangGraph, tool calling, RAG,
persistent database memory, streaming, or authentication.

## Tests

Run the automated test suite with:

```bash
pytest -q
```
