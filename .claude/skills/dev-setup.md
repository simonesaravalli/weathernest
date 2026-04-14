# Development setup

## Prerequisites
- Docker + Docker Compose v2
- Python 3.12+ (for running backend outside Docker)
- Node 20+ (for running frontend outside Docker)

## Start everything with Docker
```bash
docker compose up --build
```
- Backend: http://localhost:8000
- Frontend: http://localhost:5173
- API docs: http://localhost:8000/docs
- Postgres: localhost:5432

## Backend (without Docker)
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

## Frontend (without Docker)
```bash
cd frontend
npm install
npm run dev
```
