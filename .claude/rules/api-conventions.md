# API conventions

- All endpoints are versioned under `/api/v1/`.
- Use Pydantic schemas for all request bodies and responses — never return ORM objects directly.
- Return `snake_case` JSON keys.
- Sensor readings endpoint: `POST /api/v1/sensors/readings`
  - Must accept `device_id`, `metric` (e.g. `temperature`, `humidity`), `value`, and
    an optional `recorded_at` timestamp (defaults to server time if omitted).
  - Design the service layer so the HTTP transport can be replaced with MQTT later.
- Forecast endpoint: `GET /api/v1/forecast?lat=...&lon=...`
  - Proxies Open-Meteo; do not expose the raw Open-Meteo response shape to the frontend.
    Normalise it into the app's own schema.
