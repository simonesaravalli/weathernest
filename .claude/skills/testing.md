# Testing approach

The user is new to testing — explain the "why" when introducing test patterns.

## Backend
- Use **pytest** as the test runner.
- Use **httpx.AsyncClient** (via `pytest-asyncio`) to test API endpoints against a real
  running app instance.
- Use a **separate test database** (or SQLite in-memory for speed) — never run tests
  against the dev Postgres instance.
- Use `pytest` fixtures in `conftest.py` for the async client, DB session, and any
  shared test data.
- Aim to test: happy path, validation errors (422), not-found (404), and sensor edge cases
  (duplicate readings, out-of-range values).
- Target **≥ 80% coverage** as a baseline; don't chase 100% at the expense of test quality.

## Frontend
- **Vitest** + **React Testing Library** for component/unit tests.
- Test user interactions, not implementation details.
- Keep frontend tests simple at first — focus on backend tests to start.
