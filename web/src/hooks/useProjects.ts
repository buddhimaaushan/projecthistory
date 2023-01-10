import { useEffect, useState } from "react";
import { api } from "../api/client";
import type { Project } from "../api/types";

export function useProjects() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    api
      .listProjects()
      .then((items) => {
        if (!cancelled) {
          setProjects(items);
        }
      })
      .catch((err: unknown) => {
        if (!cancelled) {
          setError(err instanceof Error ? err.message : "could not load projects");
        }
      });
    return () => {
      cancelled = true;
    };
  }, []);

  return { projects, error };
}
