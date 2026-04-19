from datetime import datetime

from pydantic import BaseModel


class CurrentWeather(BaseModel):
    time: datetime
    temperature_c: float
    windspeed_kmh: float
    weathercode: int


class HourlyEntry(BaseModel):
    time: datetime
    temperature_c: float
    precipitation_mm: float
    weathercode: int


class ForecastResponse(BaseModel):
    latitude: float
    longitude: float
    timezone: str
    current: CurrentWeather
    hourly: list[HourlyEntry]
