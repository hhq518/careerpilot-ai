"""Small in-process memory store used to enrich chat requests."""


class MemoryManager:
    """
    Keep separate runtime memory records for each user.

    This is runtime-only memory.
    Data will be lost when the server stops.
    """

    def __init__(self) -> None:
        self._memory_store: dict[str, list[str]] = {}

    def save_memory(self, user_id: str, memory: str) -> None:
        """
        Save one memory record for a user.
        """

        cleaned_user_id = user_id.strip()
        cleaned_memory = memory.strip()

        if not cleaned_user_id:
            raise ValueError("user_id must not be empty.")

        if not cleaned_memory:
            return

        self._memory_store.setdefault(cleaned_user_id, []).append(cleaned_memory)

    def get_memory(self, user_id: str) -> list[str]:
        """
        Return memory records for a user.

        A copy is returned so callers cannot modify the internal memory list.
        """

        cleaned_user_id = user_id.strip()

        if not cleaned_user_id:
            raise ValueError("user_id must not be empty.")

        return list(self._memory_store.get(cleaned_user_id, []))