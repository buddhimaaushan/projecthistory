import { Component, ErrorInfo, ReactNode } from "react";

interface Props {
  children: ReactNode;
}

interface State {
  message: string | null;
}

export class ErrorBoundary extends Component<Props, State> {
  state: State = { message: null };

  static getDerivedStateFromError(error: unknown): State {
    return { message: error instanceof Error ? error.message : "unexpected error" };
  }

  componentDidCatch(error: Error, info: ErrorInfo) {
    console.error("dashboard crashed", error, info.componentStack);
  }

  render() {
    if (this.state.message) {
      return (
        <div className="app">
          <div className="card">
            <h2>Something went wrong</h2>
            <p className="error">{this.state.message}</p>
            <button className="button" onClick={() => window.location.reload()}>
              Reload
            </button>
          </div>
        </div>
      );
    }
    return this.props.children;
  }
}
