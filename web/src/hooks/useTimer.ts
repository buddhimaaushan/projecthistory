import { useCallback, useMemo, useState } from "react";
import { api } from "../api/client";
import type { Entry } from "../api/types";

export function useTimer(onChange: () => void) {
  const [pending, setPending] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const start = useCallback(
    async (label: string, project: string | null) => {
      setPending(true);
      try {
        await api.startTimer({ label, project });
        setError(null);
        onChange();
      } catch (err) {
        setError(err instanceof Error ? err.message : "could not start the timer");
      } finally {
        setPending(false);
      }
    },
    [onChange],
  );

  const stop = useCallback(
    async (entry: Entry) => {
      setPending(true);
      try {
        await api.stopTimer(entry.id);
        setError(null);
        onChange();
      } catch (err) {
        setError(err instanceof Error ? err.message : "could not stop the timer");
      } finally {
        setPending(false);
      }
    },
    [onChange],
  );

  return useMemo(() => ({ start, stop, pending, error }), [start, stop, pending, error]);
}
