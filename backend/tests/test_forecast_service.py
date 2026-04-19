from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest

from app.services.forecast import ForecastService, ForecastServiceError

OPEN_METEO_RESPONSE = {
    "latitude": 51.5,
    "longitude": -0.12,
    "timezone": "Europe/London",
    "current_weather": {
        "time": "2024-06-01T12:00",
        "temperature": 18.5,
        "windspeed": 14.2,
        "weathercode": 1,
    },
    "hourly": {
        "time": ["2024-06-01T00:00", "2024-06-01T01:00"],
        "temperature_2m": [15.0, 14.5],
        "precipitation": [0.0, 0.2],
        "weathercode": [0, 61],
    },
}


def _make_service(json_data: dict, status_code: int = 200) -> ForecastService:
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = status_code
    mock_response.json.return_value = json_data
    if status_code >= 400:
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            message="error", request=MagicMock(), response=mock_response
        )
    else:
        mock_response.raise_for_status.return_value = None

    client = MagicMock(spec=httpx.AsyncClient)
    client.get = AsyncMock(return_value=mock_response)
    return ForecastService(client=client)


@pytest.mark.asyncio
async def test_get_forecast_happy_path():
    service = _make_service(OPEN_METEO_RESPONSE)
    result = await service.get_forecast(51.5, -0.12)

    assert result.latitude == 51.5
    assert result.longitude == -0.12
    assert result.timezone == "Europe/London"

    assert result.current.temperature_c == 18.5
    assert result.current.windspeed_kmh == 14.2
    assert result.current.weathercode == 1

    assert len(result.hourly) == 2
    assert result.hourly[0].temperature_c == 15.0
    assert result.hourly[1].precipitation_mm == 0.2
    assert result.hourly[1].weathercode == 61


@pytest.mark.asyncio
async def test_get_forecast_http_error_raises_service_error():
    service = _make_service({}, status_code=500)
    with pytest.raises(ForecastServiceError, match="status 500"):
        await service.get_forecast(51.5, -0.12)


@pytest.mark.asyncio
async def test_get_forecast_network_error_raises_service_error():
    client = MagicMock(spec=httpx.AsyncClient)
    client.get = AsyncMock(side_effect=httpx.RequestError("connection refused"))
    service = ForecastService(client=client)
    with pytest.raises(ForecastServiceError, match="Network error"):
        await service.get_forecast(51.5, -0.12)


@pytest.mark.asyncio
async def test_get_forecast_missing_key_raises_service_error():
    incomplete = {**OPEN_METEO_RESPONSE}
    del incomplete["current_weather"]
    service = _make_service(incomplete)
    with pytest.raises(ForecastServiceError, match="Unexpected response shape"):
        await service.get_forecast(51.5, -0.12)
