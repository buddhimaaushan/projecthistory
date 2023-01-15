export function formatDuration(seconds: number): string {
  const totalMinutes = Math.floor(seconds / 60);
  const hours = Math.floor(totalMinutes / 60);
  const minutes = totalMinutes % 60;
  if (hours === 0) {
    return minutes + "m";
  }
  return hours + "h " + minutes + "m";
}

export function formatClock(seconds: number): string {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const rest = seconds % 60;
  return [hours, minutes, rest].map((part) => String(part).padStart(2, "0")).join(":");
}

export function formatPercent(value: number, total: number): string {
  if (total === 0) {
    return "0%";
  }
  return Math.round((value / total) * 100) + "%";
}
