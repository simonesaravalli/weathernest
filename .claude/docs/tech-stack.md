# Tech stack

| Layer | Choice | Notes |
|---|---|---|
| Backend language | Python 3.12+ | Use `async`/`await` throughout |
| API framework | FastAPI | Pydantic v2 for schemas |
| ORM | SQLAlchemy 2 (async) | Use `asyncpg` driver |
| Migrations | Alembic | One migration per logical change |
| Database | PostgreSQL 16 | Local: Docker; AWS: RDS |
| Frontend framework | React 18 + Vite | TypeScript preferred |
| HTTP client (FE) | TanStack Query | For data fetching + caching |
| Container runtime | Docker + Compose | See `docker-compose.yml` |
| Linting (Python) | Ruff | Replaces flake8 + isort |
| Formatting (Python) | Ruff formatter | Black-compatible |
| Type checking | mypy (strict) | Run in CI |
| Testing | pytest + httpx + pytest-asyncio | See Testing section |
