import { useMemo } from "react";
import { EntryList } from "../components/EntryList";
import { ErrorBanner } from "../components/ErrorBanner";
import { TimerCard } from "../components/TimerCard";
import { useEntries } from "../hooks/useEntries";
import { formatDuration } from "../lib/format";

export function Dashboard() {
  const { entries, loading, error, reload } = useEntries(20);
  const running = entries.find((entry) => entry.is_running);

  const todayTotal = useMemo(() => {
    const today = new Date().toDateString();
    return entries
      .filter((entry) => new Date(entry.start).toDateString() === today)
      .reduce((total, entry) => total + entry.duration_seconds, 0);
  }, [entries]);

  return (
    <div className="stack">
      <TimerCard running={running} onRefresh={reload} />
      <section className="stats">
        <div className="stat">
          <span>Today</span>
          <strong>{formatDuration(todayTotal)}</strong>
        </div>
        <div className="stat">
          <span>Entries</span>
          <strong>{entries.length}</strong>
        </div>
      </section>
      <section className="card">
        <h2>Recent entries</h2>
        {loading ? <p className="hint">Loading…</p> : null}
        <ErrorBanner message={error} />
        <EntryList entries={entries} onDelete={() => reload()} />
      </section>
    </div>
  );
}
