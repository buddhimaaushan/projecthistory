"""Prometheus instruments for the HTTP API."""

from prometheus_client import Counter, Histogram

REQUESTS = Counter(
    "tempus_http_requests_total",
    "HTTP requests handled by the API.",
    ["method", "status"],
)

LATENCY = Histogram(
    "tempus_http_request_duration_seconds",
    "Request latency in seconds.",
    ["method"],
    buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5),
)

RUNNING_TIMERS = Counter(
    "tempus_timers_started_total",
    "Timers started since the process booted.",
)
