import { NavLink, Outlet } from "react-router-dom";

const links = [
  { to: "/", label: "Dashboard", end: true },
  { to: "/entries", label: "Entries" },
  { to: "/reports", label: "Reports" },
  { to: "/settings", label: "Settings" },
];

export function Layout() {
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
      </header>
      <main>
        <Outlet />
      </main>
    </div>
  );
}
