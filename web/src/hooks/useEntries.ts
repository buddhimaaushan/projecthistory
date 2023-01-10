import { useCallback, useEffect, useState } from "react";
import { api } from "../api/client";
import type { Entry } from "../api/types";

export function useEntries(limit = 50) {
  const [entries, setEntries] = useState<Entry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const reload = useCallback(async () => {
    setLoading(true);
    try {
      setEntries(await api.listEntries(limit));
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : "could not load entries");
    } finally {
      setLoading(false);
    }
  }, [limit]);

  useEffect(() => {
    void reload();
  }, [reload]);

  return { entries, loading, error, reload };
}
