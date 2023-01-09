import { describe, expect, it } from "vitest";
import { formatClock, formatDuration, formatPercent } from "./format";

describe("formatDuration", () => {
  it("formats minutes only", () => {
    expect(formatDuration(90)).toBe("1m");
  });

  it("formats hours and minutes", () => {
    expect(formatDuration(5445)).toBe("1h 30m");
  });
});

describe("formatClock", () => {
  it("pads each part", () => {
    expect(formatClock(3661)).toBe("01:01:01");
  });
});

describe("formatPercent", () => {
  it("handles an empty total", () => {
    expect(formatPercent(10, 0)).toBe("0%");
  });
});
