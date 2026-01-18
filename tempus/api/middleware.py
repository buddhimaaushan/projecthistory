"""Small middleware helpers."""

import logging
import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware

from .. import __version__
from .metrics import LATENCY, REQUESTS

VERSION = __version__

logger = logging.getLogger("tempus.api")


class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id = request.headers.get("x-request-id", uuid.uuid4().hex[:12])
        started = time.perf_counter()
        response = await call_next(request)
        elapsed_ms = (time.perf_counter() - started) * 1000
        REQUESTS.labels(method=request.method, status=str(response.status_code)).inc()
        LATENCY.labels(method=request.method).observe(elapsed_ms / 1000)
        response.headers["x-request-id"] = request_id
        response.headers["x-tempus-version"] = VERSION
        logger.info(
            "%s %s %s %.1fms", request_id, request.method, request.url.path, elapsed_ms
        )
        return response
