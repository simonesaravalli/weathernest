# Environment variables

Managed via `pydantic-settings` (`app/core/config.py`). Always use `.env` files locally;
never hard-code secrets.

| Variable | Description |
|---|---|
| `DATABASE_URL` | Async Postgres DSN (`postgresql+asyncpg://...`) |
| `CORS_ORIGINS` | Comma-separated allowed origins for CORS |
| `SENSOR_API_KEY` | Shared secret for sensor POST authentication |
| `ENVIRONMENT` | `development` \| `production` |
