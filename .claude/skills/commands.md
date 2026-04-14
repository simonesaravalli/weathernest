# Common commands

```bash
# Run all backend tests
cd backend && pytest

# Run tests with coverage report
cd backend && pytest --cov=app --cov-report=term-missing

# Lint + format check
cd backend && ruff check . && ruff format --check .

# Auto-fix lint issues
cd backend && ruff check --fix . && ruff format .

# Type check
cd backend && mypy app

# Create a new Alembic migration
cd backend && alembic revision --autogenerate -m "describe_the_change"

# Apply migrations
cd backend && alembic upgrade head
```
