interface Props {
  title: string;
  hint?: string;
}

export function EmptyState({ title, hint }: Props) {
  return (
    <div className="empty-state">
      <strong>{title}</strong>
      {hint ? <p>{hint}</p> : null}
    </div>
  );
}
