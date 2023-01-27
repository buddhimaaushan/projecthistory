import { useState } from "react";
import { api } from "../api/client";
import type { Entry } from "../api/types";
import { EntryList } from "../components/EntryList";
import { useEntries } from "../hooks/useEntries";

export function Entries() {
  const { entries, loading, error, reload } = useEntries(200);
  const [deleteError, setDeleteError] = useState<string | null>(null);

  async function handleDelete(entry: Entry) {
    if (!window.confirm("Delete " + entry.label + "?")) {
      return;
    }
    try {
      await api.deleteEntry(entry.id);
      setDeleteError(null);
      await reload();
    } catch (err) {
      setDeleteError(err instanceof Error ? err.message : "could not delete the entry");
    }
  }

  return (
    <section className="card">
      <h2>All entries</h2>
      {loading ? <p className="hint">Loading…</p> : null}
      {error ? <p className="error">{error}</p> : null}
      {deleteError ? <p className="error">{deleteError}</p> : null}
      <EntryList entries={entries} onDelete={handleDelete} />
    </section>
  );
}
