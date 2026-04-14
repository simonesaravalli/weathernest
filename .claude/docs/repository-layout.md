# Repository layout

```
weathernest/
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI app factory
│   │   ├── core/
│   │   │   ├── config.py         # Settings via pydantic-settings
│   │   │   └── database.py       # Async SQLAlchemy engine + session
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── router.py     # Mounts all sub-routers
│   │   │       ├── forecast.py   # Open-Meteo proxy endpoints
│   │   │       ├── sensors.py    # Sensor ingestion endpoints
│   │   │       └── locations.py  # Saved locations CRUD
│   │   ├── models/               # SQLAlchemy ORM models
│   │   ├── schemas/              # Pydantic request/response schemas
│   │   └── services/             # Business logic (Open-Meteo client, etc.)
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_forecast.py
│   │   ├── test_sensors.py
│   │   └── test_locations.py
│   ├── alembic/
│   ├── alembic.ini
│   ├── pyproject.toml
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── main.tsx
│   │   ├── api/                  # TanStack Query hooks
│   │   ├── components/
│   │   └── pages/
│   ├── index.html
│   ├── vite.config.ts
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── docker-compose.prod.yml       # AWS / production overrides
└── CLAUDE.md
```
