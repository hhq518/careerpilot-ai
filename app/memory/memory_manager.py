"""Memory management utilities."""

from typing import Dict


class MemoryManager:
    """
    Manage user memories.

    This is the first simple version.
    Later it can be replaced by SQLite,
    Redis, or vector databases.
    """

    def __init__(self):
        # Temporary in-memory storage.
        # Key: user_id
        # Value: user memory text
        self._memory_store: Dict[str, str] = {}

    def save_memory(
        self,
        user_id: str,
        memory: str,
    ) -> None:
        """
        Save memory for a user.
        """

        self._memory_store[user_id] = memory

    def get_memory(
        self,
        user_id: str,
    ) -> str:
        """
        Retrieve user memory.
        """

        return self._memory_store.get(
            user_id,
            "",
        )