import logging

import httpx

from app.core.config import settings
from app.schemas.forecast import CurrentWeather, ForecastResponse, HourlyEntry

logger = logging.getLogger(__name__)


class ForecastServiceError(Exception):
    """Raised when the Open-Meteo API call fails or returns an unexpected shape."""


class ForecastService:
    def __init__(self, client: httpx.AsyncClient) -> None:
        self._client = client
        self._base_url = settings.OPEN_METEO_BASE_URL

    async def get_forecast(self, lat: float, lon: float) -> ForecastResponse:
        params: dict[str, str | float] = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": "true",
            "hourly": "temperature_2m,precipitation,weathercode",
            "timezone": "auto",
        }

        try:
            response = await self._client.get(f"{self._base_url}/forecast", params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            logger.error(
                "Open-Meteo returned %s for lat=%s lon=%s", exc.response.status_code, lat, lon
            )
            raise ForecastServiceError(
                f"Open-Meteo request failed with status {exc.response.status_code}"
            ) from exc
        except httpx.RequestError as exc:
            logger.error("Network error reaching Open-Meteo: %s", exc)
            raise ForecastServiceError("Network error reaching Open-Meteo") from exc

        try:
            data = response.json()
            current_raw = data["current_weather"]
            current = CurrentWeather(
                time=current_raw["time"],
                temperature_c=current_raw["temperature"],
                windspeed_kmh=current_raw["windspeed"],
                weathercode=current_raw["weathercode"],
            )

            hourly_raw = data["hourly"]
            hourly = [
                HourlyEntry(
                    time=time,
                    temperature_c=temp,
                    precipitation_mm=precip,
                    weathercode=code,
                )
                for time, temp, precip, code in zip(
                    hourly_raw["time"],
                    hourly_raw["temperature_2m"],
                    hourly_raw["precipitation"],
                    hourly_raw["weathercode"],
                )
            ]

            return ForecastResponse(
                latitude=data["latitude"],
                longitude=data["longitude"],
                timezone=data["timezone"],
                current=current,
                hourly=hourly,
            )
        except (KeyError, TypeError, ValueError) as exc:
            logger.error("Unexpected Open-Meteo response shape: %s", exc)
            raise ForecastServiceError("Unexpected response shape from Open-Meteo") from exc
