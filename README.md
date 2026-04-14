# WeatherNest

A self-hosted personal weather dashboard that combines live forecast data with readings from DIY home sensors.

## Features

- **Live forecasts** via [Open-Meteo](https://open-meteo.com/) (free, no API key required)
- **DIY sensor ingestion** — ESP32 / DHT22 devices push temperature and humidity readings over HTTP
- **Saved locations** — store and switch between multiple places
- **REST API** — clean versioned JSON API, fully separate from the frontend
- **Self-hosted** — runs entirely in Docker; no third-party accounts required beyond Open-Meteo

## Architecture

```
┌─────────────────┐        ┌──────────────────────┐        ┌──────────────┐
│  React frontend │ ─────▶│  FastAPI backend     │ ─────▶│  PostgreSQL  │
│  (Vite + React) │  HTTP  │  (pure REST/JSON API)│        │              │
└─────────────────┘        └──────────────────────┘        └──────────────┘
                                     ▲
                           HTTP POST │
                    ┌────────────────┘
                    │  ESP32 / DHT22 sensors (home network)
```

## Tech stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12 + FastAPI |
| Database | PostgreSQL 16 |
| ORM / migrations | SQLAlchemy 2 (async) + Alembic |
| Frontend | React 18 + Vite + TypeScript |
| Data fetching | TanStack Query |
| Linting / formatting | Ruff |
| Type checking | mypy (strict) |
| Testing | pytest + httpx + pytest-asyncio |
| Containers | Docker + Docker Compose |

## Getting started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose v2
- Git

### 1. Clone the repo

```bash
git clone https://github.com/simonesaravalli/weathernest.git
cd weathernest
```

### 2. Configure environment

```bash
cp .env.example .env
# Edit .env if needed — defaults work for local development
```

### 3. Start everything

```bash
docker compose up --build
```

| Service | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:8000 |
| API docs (Swagger) | http://localhost:8000/docs |

## Development

### Run backend without Docker

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

### Run frontend without Docker

```bash
cd frontend
npm install
npm run dev
```

### Common commands

```bash
# Tests
cd backend && pytest
cd backend && pytest --cov=app --cov-report=term-missing

# Lint & format
cd backend && ruff check . && ruff format --check .
cd backend && ruff check --fix . && ruff format .

# Type check
cd backend && mypy app

# Database migrations
cd backend && alembic revision --autogenerate -m "describe_the_change"
cd backend && alembic upgrade head
```

## Project structure

```
weathernest/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app factory
│   │   ├── core/            # Config, database session
│   │   ├── api/v1/          # Route handlers
│   │   ├── models/          # SQLAlchemy ORM models
│   │   ├── schemas/         # Pydantic request/response schemas
│   │   └── services/        # Business logic
│   ├── tests/
│   └── alembic/             # Database migrations
├── frontend/
│   └── src/
│       ├── api/             # TanStack Query hooks
│       ├── components/
│       └── pages/
├── docker-compose.yml
└── docker-compose.prod.yml  # Production overrides
```

## Sensor integration

Home sensors can push readings to the API with a simple HTTP POST:

```bash
curl -X POST http://your-server:8000/api/v1/sensors/readings \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-sensor-api-key" \
  -d '{"device_id": "esp32-living-room", "metric": "temperature", "value": 21.4}'
```

Supported metrics: `temperature`, `humidity`.

> **Roadmap:** MQTT support is planned as an alternative transport for sensors.

## Deployment

The app is designed for self-hosting. The current targets are:

- **Local / home lab** — `docker compose up` on any Docker host
- **AWS** (planned) — ECS Fargate + RDS PostgreSQL + S3/CloudFront for the frontend

## License

MIT
