import { expect, test } from "@playwright/test";

const email = "e2e-" + Date.now() + "@example.com";

test("register, sign in and see the dashboard", async ({ page, request }) => {
  const registered = await request.post("http://localhost:8000/api/auth/register", {
    data: { email, password: "correct-horse", display_name: "E2E" },
  });
  expect(registered.status()).toBe(201);

  await page.goto("/");
  await page.getByLabel("Email").fill(email);
  await page.getByLabel("Password").fill("correct-horse");
  await page.getByRole("button", { name: "Sign in" }).click();

  await expect(page.getByText("Recent entries")).toBeVisible();
  await expect(page.getByText("Sign out")).toBeVisible();
});

test("a wrong password is reported", async ({ page }) => {
  await page.goto("/");
  await page.getByLabel("Email").fill("nobody@example.com");
  await page.getByLabel("Password").fill("wrong");
  await page.getByRole("button", { name: "Sign in" }).click();
  await expect(page.getByText("incorrect email or password")).toBeVisible();
});
