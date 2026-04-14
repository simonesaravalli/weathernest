# Design decisions & rationale

- **React (Vite) over Jinja2**: Chosen to learn a modern frontend stack and keep backend
  and frontend concerns cleanly separated. The extra complexity pays off when the sensor
  dashboard needs real-time updates.
- **HTTP before MQTT for sensors**: Simpler to implement and debug first. The service layer
  is designed so MQTT can be added as an alternative ingest path without rewriting business
  logic.
- **Async SQLAlchemy**: FastAPI is async-first; a sync ORM would block the event loop under
  load. Use `asyncpg` as the driver.
- **Ruff over Black+flake8**: Single tool, much faster, covers linting and formatting.
- **Alembic for all schema changes**: Never mutate the DB schema by hand. Every change gets
  a migration file committed to the repo.
