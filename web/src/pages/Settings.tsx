import { useEffect, useState } from "react";
import { api } from "../api/client";
import type { Project } from "../api/types";

export function Settings() {
  const [projects, setProjects] = useState<Project[]>([]);

  useEffect(() => {
    api.listProjects().then(setProjects);
  }, []);

  return (
    <div className="stack">
      <section className="card">
        <h2>Projects</h2>
        <ul className="project-list">
          {projects.map((project) => (
            <li key={project.id}>
              <span className="swatch" style={{ background: project.colour }} />
              <span>{project.name}</span>
              <span className="muted">{project.archived ? "archived" : "active"}</span>
            </li>
          ))}
        </ul>
      </section>
      <section className="card">
        <h2>Connection</h2>
        <p className="hint">
          The dashboard talks to <code>VITE_API_URL</code> or the current origin. During
          development Vite proxies <code>/api</code> to port 8000.
        </p>
      </section>
    </div>
  );
}
