import type { Entry } from "../api/types";
import { shortDate } from "../lib/dates";
import { formatDuration } from "../lib/format";

interface Props {
  entries: Entry[];
  onDelete: (entry: Entry) => void;
}

export function EntryList({ entries, onDelete }: Props) {
  if (entries.length === 0) {
    return <p className="empty">No entries yet. Start the timer above.</p>;
  }

  return (
    <table className="entry-table">
      <thead>
        <tr>
          <th>Date</th>
          <th>Label</th>
          <th>Project</th>
          <th>Tags</th>
          <th>Duration</th>
          <th />
        </tr>
      </thead>
      <tbody>
        {entries.map((entry) => (
          <tr key={entry.id} className={entry.is_running ? "running" : ""}>
            <td>{shortDate(entry.start)}</td>
            <td>{entry.label}</td>
            <td>{entry.project ?? "—"}</td>
            <td>
              {entry.tags.map((tag) => (
                <span key={tag} className="tag">
                  {tag}
                </span>
              ))}
            </td>
            <td>{formatDuration(entry.duration_seconds)}</td>
            <td>
              <button className="icon-button" title="Delete" onClick={() => onDelete(entry)}>
                ×
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
