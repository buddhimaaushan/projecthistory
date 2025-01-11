"""A deliberately small fixed window limiter.

It lives in process memory, which is fine for a single container deployment. A
multi replica setup should move this to Redis; the interface is intentionally
narrow so that swap stays local.
"""

import os
import time
from collections import defaultdict

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

LIMIT = int(os.environ.get("TEMPUS_RATE_LIMIT", "240"))
WINDOW_SECONDS = 60


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, limit: int = LIMIT, window: int = WINDOW_SECONDS):
        super().__init__(app)
        self.limit = limit
        self.window = window
        self.buckets = defaultdict(lambda: [0, 0.0])

    async def dispatch(self, request, call_next):
        if request.url.path in ("/health", "/metrics"):
            return await call_next(request)
        client = request.client.host if request.client else "unknown"
        count, started = self.buckets[client]
        now = time.monotonic()
        if now - started > self.window:
            count, started = 0, now
        count += 1
        self.buckets[client] = [count, started]
        if count > self.limit:
            return JSONResponse(
                status_code=429,
                content={"detail": "too many requests"},
                headers={"Retry-After": str(int(self.window - (now - started)) + 1)},
            )
        return await call_next(request)
