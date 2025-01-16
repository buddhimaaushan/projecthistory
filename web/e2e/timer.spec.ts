import { expect, test } from "@playwright/test";

test("start and stop a timer", async ({ page, request }) => {
  const email = "timer-" + Date.now() + "@example.com";
  await request.post("http://localhost:8000/api/auth/register", {
    data: { email, password: "correct-horse", display_name: "Timer" },
  });

  await page.goto("/");
  await page.getByLabel("Email").fill(email);
  await page.getByLabel("Password").fill("correct-horse");
  await page.getByRole("button", { name: "Sign in" }).click();
  await expect(page.getByText("Recent entries")).toBeVisible();

  await page.getByPlaceholder("What are you working on?").fill("e2e writing");
  await page.getByRole("button", { name: "Start" }).click();
  await expect(page.getByText("e2e writing")).toBeVisible();
  await page.getByRole("button", { name: "Stop" }).click();
  await expect(page.getByRole("button", { name: "Start" })).toBeVisible();
});
