import { useEffect, useState } from "react";
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { api, getToken, setToken } from "./api/client";
import type { User } from "./api/types";
import { ErrorBoundary } from "./components/ErrorBoundary";
import { Layout } from "./components/Layout";
import { Dashboard } from "./pages/Dashboard";
import { Entries } from "./pages/Entries";
import { Login } from "./pages/Login";
import { Reports } from "./pages/Reports";
import { Settings } from "./pages/Settings";

function AppRoutes() {
  const [user, setUser] = useState<User | null>(null);
  const [ready, setReady] = useState(false);

  async function loadUser() {
    if (!getToken()) {
      setUser(null);
      setReady(true);
      return;
    }
    try {
      setUser(await api.me());
    } catch {
      setToken(null);
      setUser(null);
    } finally {
      setReady(true);
    }
  }

  useEffect(() => {
    void loadUser();
  }, []);

  if (!ready) {
    return <p className="hint">Loading…</p>;
  }

  if (!user) {
    return <Login onSuccess={() => void loadUser()} />;
  }

  return (
    <Routes>
      <Route element={<Layout user={user} onLogout={() => { setToken(null); setUser(null); }} />}>
        <Route index element={<Dashboard />} />
        <Route path="entries" element={<Entries />} />
        <Route path="reports" element={<Reports />} />
        <Route path="settings" element={<Settings />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
  );
}

export default function App() {
  return (
    <ErrorBoundary>
      <BrowserRouter>
        <AppRoutes />
      </BrowserRouter>
    </ErrorBoundary>
  );
}
