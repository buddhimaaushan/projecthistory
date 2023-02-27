import { useEffect, useRef, useState } from "react";
import type { Entry } from "../api/types";
import { useTimer } from "../hooks/useTimer";
import { formatClock, formatDuration } from "../lib/format";
import { ProjectSelect } from "./ProjectSelect";

interface Props {
  running: Entry | undefined;
  onRefresh: () => void;
}

export function TimerCard({ running, onRefresh }: Props) {
  const [label, setLabel] = useState("");
  const [project, setProject] = useState<string | null>(null);
  const [elapsed, setElapsed] = useState(running?.duration_seconds ?? 0);
  const timer = useTimer(onRefresh);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    function onKeyDown(event: KeyboardEvent) {
      if (event.key === "n" && document.activeElement?.tagName !== "INPUT") {
        inputRef.current?.focus();
      }
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, []);

  useEffect(() => {
    setElapsed(running?.duration_seconds ?? 0);
    if (!running) {
      return;
    }
    const started = Date.now() - running.duration_seconds * 1000;
    const handle = window.setInterval(() => {
      setElapsed(Math.floor((Date.now() - started) / 1000));
    }, 1000);
    return () => window.clearInterval(handle);
  }, [running]);

  if (running) {
    return (
      <section className="card timer-card running">
        <div>
          <span className="timer-label">{running.label}</span>
          <span className="timer-project">{running.project ?? "unassigned"}</span>
        </div>
        <strong className="timer-clock">{formatClock(elapsed)}</strong>
        <button className="button danger" disabled={timer.pending} onClick={() => void timer.stop(running)}>
          Stop
        </button>
        {timer.error ? <p className="error">{timer.error}</p> : null}
      </section>
    );
  }

  return (
    <section className="card timer-card">
      <form
        className="timer-form"
        onSubmit={(event) => {
          event.preventDefault();
          if (label.trim()) {
            void timer.start(label.trim(), project);
            setLabel("");
          }
        }}
      >
        <input
          ref={inputRef}
          className="input"
          placeholder="What are you working on?"
          value={label}
          onChange={(event) => setLabel(event.target.value)}
        />
        <ProjectSelect value={project} onChange={setProject} />
        <button className="button" type="submit" disabled={timer.pending || !label.trim()}>
          Start
        </button>
      </form>
      {timer.error ? <p className="error">{timer.error}</p> : null}
      <p className="hint">Last entry: {formatDuration(0)} today</p>
    </section>
  );
}
