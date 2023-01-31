import { useEffect, useState } from "react";
import { api } from "../api/client";
import type { Summary } from "../api/types";
import { WeeklyChart } from "../components/WeeklyChart";
import { formatDuration, formatPercent } from "../lib/format";

export function Reports() {
  const [summary, setSummary] = useState<Summary | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api
      .summary()
      .then(setSummary)
      .catch((err: unknown) => setError(err instanceof Error ? err.message : "could not load reports"));
  }, []);

  if (error) {
    return <p className="error">{error}</p>;
  }
  if (!summary) {
    return <p className="hint">Loading…</p>;
  }

  return (
    <div className="stack">
      <section className="stats">
        <div className="stat">
          <span>Total</span>
          <strong>{formatDuration(summary.total_seconds)}</strong>
        </div>
        <div className="stat">
          <span>Entries</span>
          <strong>{summary.entries}</strong>
        </div>
      </section>
      <section className="card">
        <h2>Last seven days</h2>
        <WeeklyChart byDay={summary.by_day} />
      </section>
      <section className="card">
        <h2>By project</h2>
        <ul className="project-list">
          {Object.entries(summary.by_project).map(([name, seconds]) => (
            <li key={name}>
              <span>{name}</span>
              <span>{formatDuration(seconds)}</span>
              <span className="muted">{formatPercent(seconds, summary.total_seconds)}</span>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
