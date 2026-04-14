# Architecture

```
┌─────────────────┐        ┌──────────────────────┐        ┌──────────────┐
│  React frontend │ ──────▶│  FastAPI backend      │ ──────▶│  PostgreSQL  │
│  (Vite + React) │  HTTP  │  (pure REST/JSON API) │        │              │
└─────────────────┘        └──────────────────────┘        └──────────────┘
                                     ▲
                           HTTP POST │
                    ┌────────────────┘
                    │  ESP32 / DHT22 sensors (home network)
```

- The **frontend** is a standalone React (Vite) app. It talks to the backend only via the
  REST API — no server-side rendering.
- The **backend** is a pure FastAPI JSON API. It fetches forecasts from Open-Meteo and
  receives sensor readings from IoT devices.
- **MQTT** is a planned future addition for sensor ingestion (learning goal). For now, sensors
  POST over HTTP. Design the sensor ingestion layer so the transport can be swapped later.
