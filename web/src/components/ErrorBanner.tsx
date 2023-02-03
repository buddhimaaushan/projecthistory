interface Props {
  message: string | null;
  onDismiss?: () => void;
}

export function ErrorBanner({ message, onDismiss }: Props) {
  if (!message) {
    return null;
  }
  return (
    <div className="banner error" role="alert">
      <span>{message}</span>
      {onDismiss ? (
        <button className="icon-button" onClick={onDismiss} aria-label="Dismiss">
          ×
        </button>
      ) : null}
    </div>
  );
}
