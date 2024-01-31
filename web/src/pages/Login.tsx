import { useState, type FormEvent } from "react";
import { login } from "../api/client";

interface Props {
  onSuccess: () => void;
}

export function Login({ onSuccess }: Props) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [pending, setPending] = useState(false);

  async function submit(event: FormEvent) {
    event.preventDefault();
    setPending(true);
    try {
      await login(email, password);
      setError(null);
      onSuccess();
    } catch (err) {
      setError(err instanceof Error ? err.message : "could not sign in");
    } finally {
      setPending(false);
    }
  }

  return (
    <div className="app login-screen">
      <form className="card login-card" onSubmit={(event) => void submit(event)}>
        <h1>tempus</h1>
        <p>Sign in to see your tracked time.</p>
        <label className="field">
          <span>Email</span>
          <input className="input" type="email" value={email} onChange={(event) => setEmail(event.target.value)} required />
        </label>
        <label className="field">
          <span>Password</span>
          <input className="input" type="password" value={password} onChange={(event) => setPassword(event.target.value)} required />
        </label>
        {error ? <p className="error">{error}</p> : null}
        <button className="button" type="submit" disabled={pending}>
          {pending ? "Signing in…" : "Sign in"}
        </button>
      </form>
    </div>
  );
}
