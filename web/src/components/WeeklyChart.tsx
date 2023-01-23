import { Bar, BarChart, CartesianGrid, Tooltip, XAxis, YAxis } from "recharts";
import { weekdayLabel } from "../lib/dates";
import { formatDuration } from "../lib/format";

interface Props {
  byDay: Record<string, number>;
}

export function WeeklyChart({ byDay }: Props) {
  const data = Object.entries(byDay).map(([day, seconds]) => ({
    day: weekdayLabel(day),
    hours: Math.round((seconds / 3600) * 10) / 10,
  }));

  if (data.length === 0) {
    return <p className="empty">Nothing recorded in this range.</p>;
  }

  return (
    <BarChart width={640} height={240} data={data} margin={{ top: 8, right: 8, bottom: 8, left: 0 }}>
      <CartesianGrid strokeDasharray="3 3" vertical={false} />
      <XAxis dataKey="day" tickLine={false} axisLine={false} />
      <YAxis tickLine={false} axisLine={false} width={40} />
      <Tooltip formatter={(value: number) => formatDuration(value * 3600)} />
      <Bar dataKey="hours" fill="var(--accent)" radius={[4, 4, 0, 0]} />
    </BarChart>
  );
}
