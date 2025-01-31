# Observability

The API exposes two endpoints that are not part of the public schema:

- `GET /health` runs a trivial query so a failing database is visible to the
  load balancer.
- `GET /metrics` returns Prometheus text format.

## Metrics

| Metric | Labels | Meaning |
| --- | --- | --- |
| `tempus_http_requests_total` | method, status | Request counter |
| `tempus_http_request_duration_seconds` | method | Latency histogram |
| `tempus_timers_started_total` | — | Started timers |

## Logs

Set `TEMPUS_LOG_JSON=1` to emit one JSON object per line. Every request logs a
short request id which is also returned in the `x-request-id` header, so a
browser report can be matched to a server line.

## Limitations

The rate limiter keeps counters in process memory. With more than one API
replica the effective limit multiplies; move the bucket to Redis before scaling
out.
