"""Tiny TTL cache used for expensive read endpoints."""

import time
from typing import Any, Dict, Hashable, Tuple


class TTLCache:
    def __init__(self, ttl_seconds: float = 30.0):
        self.ttl = ttl_seconds
        self._data: Dict[Hashable, Tuple[float, Any]] = {}

    def get(self, key: Hashable):
        item = self._data.get(key)
        if item is None:
            return None
        stored_at, value = item
        if time.monotonic() - stored_at > self.ttl:
            self._data.pop(key, None)
            return None
        return value

    def set(self, key: Hashable, value: Any) -> None:
        self._data[key] = (time.monotonic(), value)

    def invalidate(self) -> None:
        self._data.clear()

    def __len__(self) -> int:
        return len(self._data)


summary_cache = TTLCache(ttl_seconds=30.0)
