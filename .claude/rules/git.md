# Git Rules

## Commit message format
Use Conventional Commits: https://www.conventionalcommits.org

Format: <type>(<scope>): <short description>

Types:
- feat: a new feature
- fix: a bug fix
- chore: maintenance, dependencies, config changes
- docs: documentation only
- test: adding or updating tests
- refactor: code change that is not a fix or feature
- style: formatting, missing semicolons, etc.

Examples:
- feat(sensors): add POST /api/v1/sensors/readings endpoint
- fix(forecast): handle Open-Meteo timeout gracefully
- chore(deps): upgrade FastAPI to 0.111
- docs(claude): add git workflow rules

## Branch naming
Format: <type>/<short-description>

Examples:
- feat/sensor-ingestion
- fix/forecast-timeout
- chore/docker-compose-cleanup

## Rules
- Never commit .env files — only .env.example
- Never commit secrets, API keys, or credentials of any kind
- Never commit directly to main — always use a feature branch
- Always run tests before committing: cd backend && pytest
- Always run linter before committing: cd backend && ruff check .
- One logical change per commit — do not bundle unrelated changes
- If a migration is added, it must be committed together with the
  model change that caused it — never in a separate commit
