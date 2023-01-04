export interface Entry {
  id: number;
  label: string;
  project: string | null;
  tags: string[];
  start: string;
  end: string | null;
  duration_seconds: number;
  is_running: boolean;
}

export interface Project {
  id: number;
  name: string;
  colour: string;
  archived: boolean;
}

export interface Summary {
  entries: number;
  total_seconds: number;
  by_project: Record<string, number>;
  by_day: Record<string, number>;
}

export interface EntryPayload {
  label: string;
  project?: string | null;
  tags?: string[];
}
