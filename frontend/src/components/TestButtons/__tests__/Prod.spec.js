import { test, expect } from '@playwright/test';
import '../GetApiMessage/__tests__/Prod.spec.js';
import '../GetSupabaseHealth/__tests__/Prod.spec.js';
import '../GenerateJwt/__tests__/Prod.spec.js';
import '../GenerateUserLifecycle/__tests__/Prod.spec.js';

// This file serves as the entry point for all production environment tests
// Individual component tests are imported from their respective directories above
test.describe('Production Environment Setup', () => {
  test.beforeEach(async ({ page }) => {
    // Navigate to production environment
    await page.goto('https://team5-frontend-eu-f40f1bfc04e7.herokuapp.com/');
    await expect(page).toHaveTitle(/Vite \+ React/);
  });
});
