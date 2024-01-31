import type { Entry, EntryPayload, Project, Summary } from "./types";

const BASE_URL = import.meta.env.VITE_API_URL ?? "";
const TOKEN_KEY = "tempus.token";

export class ApiError extends Error {
  status: number;

  constructor(status: number, message: string) {
    super(message);
    this.status = status;
  }
}

export function getToken(): string | null {
  return localStorage.getItem(TOKEN_KEY);
}

export function setToken(token: string | null): void {
  if (token) {
    localStorage.setItem(TOKEN_KEY, token);
  } else {
    localStorage.removeItem(TOKEN_KEY);
  }
}

function authHeaders(): Record<string, string> {
  const token = getToken();
  return token ? { Authorization: "Bearer " + token } : {};
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(BASE_URL + path, {
    headers: { "Content-Type": "application/json", ...authHeaders() },
    ...init,
  });
  if (!response.ok) {
    let detail = response.statusText;
    try {
      const body = await response.json();
      detail = body.detail ?? detail;
    } catch {
      // The server did not send JSON; keep the status text.
    }
    throw new ApiError(response.status, detail);
  }
  if (response.status === 204) {
    return undefined as T;
  }
  return (await response.json()) as T;
}

export async function login(email: string, password: string): Promise<string> {
  const body = new URLSearchParams({ username: email, password });
  const response = await fetch(BASE_URL + "/api/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body,
  });
  if (!response.ok) {
    throw new ApiError(response.status, "incorrect email or password");
  }
  const data = (await response.json()) as { access_token: string };
  setToken(data.access_token);
  return data.access_token;
}

export const api = {
  me(): Promise<import("./types").User> {
    return request("/api/auth/me");
  },
  listEntries(limit = 50, offset = 0): Promise<Entry[]> {
    return request("/api/entries?limit=" + limit + "&offset=" + offset);
  },
  createEntry(payload: EntryPayload): Promise<Entry> {
    return request("/api/entries", { method: "POST", body: JSON.stringify(payload) });
  },
  startTimer(payload: EntryPayload): Promise<Entry> {
    return request("/api/entries/start", { method: "POST", body: JSON.stringify(payload) });
  },
  stopTimer(id: number): Promise<Entry> {
    return request("/api/entries/" + id + "/stop", { method: "POST" });
  },
  deleteEntry(id: number): Promise<void> {
    return request("/api/entries/" + id, { method: "DELETE" });
  },
  listProjects(): Promise<Project[]> {
    return request("/api/projects");
  },
  summary(): Promise<Summary> {
    return request("/api/reports/summary");
  },
};
