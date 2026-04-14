# Deployment

## Local (Docker lab)
- `docker-compose.yml` is the source of truth.
- Postgres data is persisted in a named volume.

## AWS (future)
- Backend: ECS Fargate (or EC2 if simpler at first)
- Database: RDS PostgreSQL
- Frontend: S3 + CloudFront
- Container images: ECR
- Secrets: AWS Secrets Manager (map to the same env var names above)
- `docker-compose.prod.yml` will hold production-specific overrides.
