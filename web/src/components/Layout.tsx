import { NavLink, Outlet } from "react-router-dom";
import { useTheme } from "../hooks/useTheme";
import { OfflineBanner } from "./OfflineBanner";

const links = [
  { to: "/", label: "Dashboard", end: true },
  { to: "/entries", label: "Entries" },
  { to: "/reports", label: "Reports" },
  { to: "/settings", label: "Settings" },
];

import type { User } from "../api/types";

interface Props {
  user: User | null;
  onLogout: () => void;
}

export function Layout({ user, onLogout }: Props) {
  const { theme, toggle } = useTheme();

  return (
    <div className="app">
      <header className="topbar">
        <h1 className="brand">tempus</h1>
        <nav className="nav">
          {links.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              end={link.end}
              className={({ isActive }) => (isActive ? "nav-link active" : "nav-link")}
            >
              {link.label}
            </NavLink>
          ))}
        </nav>
        <button className="link-button" onClick={toggle} aria-label="Toggle theme">
          {theme === "dark" ? "Light mode" : "Dark mode"}
        </button>
        {user ? (
          <div className="account">
            <span>{user.display_name || user.email}</span>
            <button className="link-button" onClick={onLogout}>
              Sign out
            </button>
          </div>
        ) : null}
      </header>
      <main>
        <OfflineBanner />
        <Outlet />
      </main>
    </div>
  );
}
