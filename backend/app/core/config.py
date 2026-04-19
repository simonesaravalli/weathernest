from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DATABASE_URL: str = "postgresql+asyncpg://weathernest:password@localhost:5432/weathernest"
    CORS_ORIGINS: str = "http://localhost:5173"
    SENSOR_API_KEY: str = "change-me"
    ENVIRONMENT: str = "development"
    OPEN_METEO_BASE_URL: str = "https://api.open-meteo.com/v1"


settings = Settings()
