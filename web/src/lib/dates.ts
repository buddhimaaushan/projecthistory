import { format, parseISO, startOfWeek } from "date-fns";

export function shortDate(iso: string): string {
  return format(parseISO(iso), "d MMM");
}

export function weekdayLabel(iso: string): string {
  return format(parseISO(iso), "EEE");
}

export function startOfCurrentWeek(): string {
  return format(startOfWeek(new Date(), { weekStartsOn: 1 }), "yyyy-MM-dd");
}

export function today(): string {
  return format(new Date(), "yyyy-MM-dd");
}
