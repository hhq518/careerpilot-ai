"""Small in-process memory store used to enrich chat requests."""


class MemoryManager:
    """Keep separate runtime memory records for each user."""

    def __init__(self) -> None:
        """Create an empty memory store."""

        self._memories: dict[str, list[str]] = {}

    def add_memory(self, user_id: str, memory: str) -> None:
        """Append one memory record for a user."""

        self._memories.setdefault(user_id, []).append(memory)

    def get_memory(self, user_id: str) -> list[str]:
        """Return a copy of a user's records, or an empty list when unknown."""

        return list(self._memories.get(user_id, []))
