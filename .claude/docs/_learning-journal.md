# WeatherNest — Claude Code Learning Journal

> A step-by-step record of building WeatherNest using Claude Code, from first prompt to
> deployment. Intended as a reference and teaching guide for colleagues learning the full
> Claude Code development lifecycle.

---

## What is this document?

This journal documents the complete development lifecycle of **WeatherNest** — a personal
weather dashboard that combines Open-Meteo forecast data with DIY home sensor readings
(ESP32 + DHT22).

The app itself is simple by design. The real goal is to learn and demonstrate:

- How to use Claude Code across a full project lifecycle
- How to write an effective `CLAUDE.md`
- How to use imports, rules, skills, and docs to structure Claude Code's context
- How to go from planning → code → local Docker deployment → AWS deployment

---

## The Application

**WeatherNest** displays weather data (temperature, humidity, etc.) for specific locations
using the free [Open-Meteo API](https://open-meteo.com/). It is designed to later ingest
readings from DIY home sensors (ESP32 + DHT22) via a REST API endpoint.

### Tech stack

| Layer | Choice | Why |
|---|---|---|
| Backend | Python 3.12 + FastAPI | Async-first, clean API design, widely known |
| Database | PostgreSQL 16 | Reliable, standard, RDS-ready for AWS |
| ORM | SQLAlchemy 2 (async) + Alembic | Production-grade, migration support |
| Frontend | React 18 + Vite + TypeScript | Modern stack, clean separation from backend |
| HTTP client (FE) | TanStack Query | Data fetching + caching |
| Linting/formatting | Ruff | Single tool, replaces flake8 + black + isort |
| Containers | Docker + Compose | Local lab + AWS deployment path |
| Cloud | AWS ECS Fargate + RDS + S3/CloudFront | Real AWS, minimal ops overhead |

---

## Project Roadmap

| Phase | Status | Topic |
|---|---|---|
| Phase 0 | ✅ Complete | Claude Code setup & first CLAUDE.md |
| Phase 1 | ✅ Complete | Architecture planning & scaffolding |
| Phase 2 | ✅ Complete | CLAUDE.md deep dive (imports, rules, skills, docs) |
| Phase 3 | ⏳ Pending | Iterative code generation |
| Phase 4 | ⏳ Pending | Local deployment with Docker |
| Phase 5 | ⏳ Pending | Cloud deployment on AWS |
| Phase 6 | ⏳ Pending | ESP32 sensor ingestion |
| Phase 7 | ⏳ Pending | Retrospective & teaching synthesis |

---

## ✅ Phase 0 — Claude Code Setup & First CLAUDE.md

*Concepts: Claude Code installation, project initialization, first CLAUDE.md*

### Before starting

Create an empty folder called `weathernest` and run `claude` inside it. A clean slate
makes the lesson clearer — you will see exactly what Claude Code contributes from scratch.

```bash
mkdir weathernest
cd weathernest
claude
```

### Prompt

```
I'm starting a new project. Before we write any code, help me create an initial
CLAUDE.md for a Python FastAPI weather dashboard app. Ask me questions to
understand the project before generating it.
```

### How the conversation went

Claude Code asked two rounds of questions before generating anything.

**First round — core requirements:**

| # | Question | Answer given |
|---|---|---|
| 1 | Data sources | Open-Meteo; in the future also DIY sensors (ESP32 + DHT22 temp/humidity) at home |
| 2 | Frontend approach | Frontend + FastAPI as a pure API backend (React/Vue — don't know them, prefer this over alternatives) |
| 3 | Data persistence | A database is required |
| 4 | Testing | I want testing in place. I know almost nothing so I need help choosing tools, defining tests, and running them |
| 5 | Deployment | Docker lab first, then AWS |
| 6 | Linting/formatting | Help me choose — no preference |

**Second round — Claude Code asked for more detail:**

| Topic | Answer given |
|---|---|
| Frontend framework | Pick one of your choice |
| Database | Go with Postgres |
| Sensor ingestion | POST directly to a FastAPI endpoint — HTTP or MQTT, maybe MQTT for learning |
| Linting/formatting | I honestly have no idea, I trust your choice |

Claude Code then generated the initial `CLAUDE.md`.

### Teaching notes

> 💡 Notice how saying *"ask me questions before generating"* completely changes the output
> quality. Claude Code could have generated a generic CLAUDE.md immediately — instead it
> interviewed you first. Always slow it down at the start of a project.

> 💡 When you don't know something (linting tools, frontend framework), it is perfectly
> valid to say *"I trust your choice"*. Claude Code will pick sensible defaults and document
> the reasoning. You can always change it later.

> 💡 The answers you give here directly shape every future Claude Code session. Vague
> answers produce vague guidance. Specific answers — even if uncertain — produce actionable
> CLAUDE.md content.

### Key lesson

**Claude Code has no memory between sessions. CLAUDE.md is how you give it a brain.**

---

## ✅ Phase 1 — Architecture Planning & Scaffolding

*Concepts: Using Claude Code as a thinking partner, not just a code generator*

### Before prompting

At the end of Phase 0, Claude Code will likely say something like:

> *"Ready to start scaffolding the project structure whenever you are."*

**Do not let it proceed yet.** Phase 1 starts with a deliberate pause. Claude Code wants
to jump to doing — your job is to make it think first.

### Prompt — architecture first

```
Not yet. Before scaffolding anything, I want to discuss the architecture.
Let's think through the high-level design of the app first. Ask me questions
to understand requirements, then propose an architecture and wait for my
approval before touching any files.
```

Review Claude Code's proposed architecture. Make sure it covers:

- How the frontend, backend, and database relate to each other
- How Open-Meteo data flows through the system
- Where ESP32 sensor data enters (even if unused initially)
- Why key decisions were made (this becomes `decisions.md` later)

Once you are happy with the architecture and it is reflected in CLAUDE.md:

### Prompt — scaffold

```
Ok, now scaffold the project structure based on the repository layout
in CLAUDE.md. Create the folders and empty placeholder files, but no
real code yet.
```

### What was created

```
weathernest/
├── .env.example
├── .gitignore
├── CLAUDE.md
├── docker-compose.yml
├── docker-compose.prod.yml
├── backend/
│   ├── .env.example
│   ├── Dockerfile
│   ├── alembic.ini
│   ├── pyproject.toml
│   ├── alembic/
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions/           ← empty, tracked via .gitkeep
│   ├── app/
│   │   ├── main.py
│   │   ├── core/config.py
│   │   ├── core/database.py
│   │   ├── api/v1/router.py
│   │   ├── api/v1/forecast.py
│   │   ├── api/v1/sensors.py
│   │   ├── api/v1/locations.py
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   └── tests/
│       ├── conftest.py
│       ├── test_forecast.py
│       ├── test_sensors.py
│       └── test_locations.py
└── frontend/
    ├── Dockerfile
    ├── index.html
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    └── src/
        ├── main.tsx
        ├── api/
        ├── components/
        └── pages/
```

Notable details Claude Code handled automatically:
- Every Python directory has an `__init__.py` (proper packages)
- `pyproject.toml` consolidates all tool config (Ruff, mypy, pytest) — no separate config files
- `.gitignore` is fully functional immediately after `git init`
- Two `.env.example` files: root uses `db` as hostname (Docker), backend uses `localhost` (local dev)

### Teaching notes

> 💡 The first prompt here is as important as the second one. Without explicitly telling
> Claude Code to think before acting, it would have started generating files immediately.
> The habit of *propose before implement* is what separates a productive Claude Code
> workflow from a chaotic one.

> 💡 Notice that the scaffold matches the repository layout in CLAUDE.md exactly. Claude
> Code used it as the source of truth rather than making its own structural decisions. This
> is CLAUDE.md working as intended.

> 💡 Watch for things Claude Code does that you did not explicitly ask for — like the two
> `.env.example` files with different hostnames. When it does something smart unprompted,
> that is usually a sign that your CLAUDE.md rules were clear enough to guide it.

### Key lesson

**Always make Claude Code propose before it implements. Slow it down and make it think first.**

---

## ✅ Phase 2 — CLAUDE.md Deep Dive

*Concepts: Imports, rules, skills, docs — the four pillars*

### Before prompting

At this point `CLAUDE.md` is a single long file with everything in it. That works for a
small project but becomes unmaintainable as the codebase grows. Phase 2 breaks it apart
into a modular system.

### The four pillars

| Pillar | Purpose | Example |
|---|---|---|
| **Rules** | Instructions Claude Code must follow | "Never call `session.commit()` in route handlers" |
| **Docs** | Reference material Claude Code should be aware of | Architecture diagram, API conventions |
| **Skills** | Step-by-step procedures for repeatable tasks | "How to add a new API endpoint" |
| **Imports** | `@` references that pull other files into CLAUDE.md | `@.claude/rules/python.md` |

### Prompt

```
Let's refactor CLAUDE.md into a modular structure. Do not change any content
yet — just help me create the folder structure .claude/docs/, .claude/skills/,
and .claude/rules/, then we will move content into them one section at a time.
Start by showing me the plan before creating anything.
```

### What was created

```
.claude/
├── docs/
│   ├── overview.md
│   ├── architecture.md
│   ├── tech-stack.md
│   ├── repository-layout.md
│   ├── environment-variables.md
│   ├── deployment.md
│   └── decisions.md
├── skills/
│   ├── dev-setup.md
│   ├── commands.md
│   └── testing.md
└── rules/
    ├── workflow.md
    ├── api-conventions.md
    └── avoid.md
```

### The final CLAUDE.md (index file)

```markdown
# WeatherNest — CLAUDE.md

Project-level guidance for Claude Code. Read this before touching any code.

## Rules
@.claude/rules/workflow.md
@.claude/rules/api-conventions.md
@.claude/rules/avoid.md

## Docs
@.claude/docs/overview.md
@.claude/docs/architecture.md
@.claude/docs/tech-stack.md
@.claude/docs/repository-layout.md
@.claude/docs/environment-variables.md
@.claude/docs/deployment.md
@.claude/docs/decisions.md

## Skills
@.claude/skills/dev-setup.md
@.claude/skills/commands.md
@.claude/skills/testing.md
```

Note that:
- **Rules are listed first** — Claude Code reads them before any reference material
- **No `---` dividers** between imports — they add visual noise without adding meaning
- **Grouped by type** — makes it immediately clear to any reader what each file's purpose is

### Teaching notes

> 💡 The phrase *"do not change any content yet"* is critical. Without it, Claude Code
> might refactor and restructure content simultaneously — making it hard to verify nothing
> was lost. Always separate structure changes from content changes.

> 💡 Rules, docs, and skills serve different purposes. Rules are instructions Claude Code
> must follow. Docs are reference material it should be aware of. Skills are step-by-step
> procedures for repeatable tasks. Keeping them separate makes it easy to update one
> without touching the others.

> 💡 A practical rule of thumb for the future: *create a skill when you find yourself
> explaining the same thing to Claude Code twice; create a rule when Claude Code does
> something wrong once.*

> 💡 CLAUDE.md is now just an index. Any new pattern, convention, or procedure that
> emerges during development gets its own file and one new line in CLAUDE.md. This scales
> indefinitely without the index ever becoming unwieldy.

### Key lesson

**A well-structured CLAUDE.md is the difference between Claude Code needing constant
hand-holding vs. already knowing your codebase.**

---

## ⏳ Phase 3 — Iterative Code Generation

*Concepts: Prompting strategy, task decomposition, reviewing Claude's output*

Build the app one layer at a time — never ask Claude Code to build everything at once.

### Recommended order

1. **Data layer** — service that fetches weather from Open-Meteo for configured locations
2. **Backend API** — REST endpoints for forecast, locations, and sensor ingestion
3. **Database layer** — SQLAlchemy models, Pydantic schemas, first Alembic migration
4. **Frontend** — React dashboard displaying temperature, humidity, and other metrics
5. **Configuration** — locations defined in config, not hardcoded

### Key lesson

**Claude Code works best with small, focused tasks. Big vague prompts produce big vague code.**

---

## ⏳ Phase 4 — Local Deployment with Docker

*Concepts: Containerization, Docker Compose, environment variables, local testing*

- Validate and complete `Dockerfile` for backend and frontend
- Complete `docker-compose.yml` for the full local stack
- Run and verify the full app locally
- Add a "how to run locally" skill to CLAUDE.md
- Learn how to keep Docker config in sync with app changes using Claude Code

### Key lesson

**CLAUDE.md should evolve as the project grows. Every new pattern is a candidate for a
new rule or skill.**

---

## ⏳ Phase 5 — Cloud Deployment on AWS

*Concepts: Infrastructure as code basics, ECS Fargate, secrets management*

- Choose deployment target (App Runner for simplicity, ECS Fargate for realism)
- Use Claude Code to generate deployment scripts or basic Terraform/CDK config
- Manage secrets via AWS Secrets Manager, mapped to the same env var names
- Complete `docker-compose.prod.yml` with ECR images and production settings
- Add a "how to deploy to AWS" skill to CLAUDE.md

### Key lesson

**Claude Code can generate infrastructure code too — but it needs clear rules about your
cloud environment in CLAUDE.md to stay consistent.**

---

## ⏳ Phase 6 — Future-Proofing: ESP32 Sensor Ingestion

*Concepts: Designing for extensibility from the start*

- Verify the `/api/v1/sensors/readings` endpoint is ready to receive DHT22 payloads
- Document the expected JSON payload format
- Test the endpoint manually (curl or Postman) before connecting a real device
- Add a "future scope: MQTT" note to `decisions.md` so it is never accidentally removed

### Expected sensor payload

```json
{
  "device_id": "esp32-living-room",
  "metric": "temperature",
  "value": 21.4,
  "recorded_at": "2025-04-14T10:30:00Z"
}
```

### Key lesson

**CLAUDE.md is also a contract with your future self and future Claude sessions.**

---

## ⏳ Phase 7 — Retrospective & Teaching Synthesis

*Concepts: Distilling what you learned into something teachable*

- Review the final CLAUDE.md system and reflect on how it evolved across phases
- Write a short "lessons learned" document to share with colleagues
- Identify the 3–5 most impactful practices to highlight in a team presentation

### Key lesson

**The best way to solidify what you learned is to teach it. This phase is the real deliverable.**

---

## Quick Reference — Prompts Used

| Phase | Prompt |
|---|---|
| Phase 0 | `I'm starting a new project. Before we write any code, help me create an initial CLAUDE.md for a Python FastAPI weather dashboard app. Ask me questions to understand the project before generating it.` |
| Phase 1 (hold) | `Not yet. Before scaffolding anything, I want to discuss the architecture. Let's think through the high-level design of the app first. Ask me questions to understand requirements, then propose an architecture and wait for my approval before touching any files.` |
| Phase 1 (scaffold) | `Ok, now scaffold the project structure based on the repository layout in CLAUDE.md. Create the folders and empty placeholder files, but no real code yet.` |
| Phase 2 | `Let's refactor CLAUDE.md into a modular structure. Do not change any content yet — just help me create the folder structure .claude/docs/, .claude/skills/, and .claude/rules/, then we will move content into them one section at a time. Start by showing me the plan before creating anything.` |

---

## Key Lessons Summary

| Phase | Lesson |
|---|---|
| 0 | Claude Code has no memory between sessions. CLAUDE.md is how you give it a brain. |
| 1 | Always make Claude Code propose before it implements. Slow it down and make it think first. |
| 2 | A well-structured CLAUDE.md is the difference between hand-holding and a self-sufficient collaborator. |
| 3 | Small, focused tasks produce better code than big vague prompts. |
| 4 | CLAUDE.md should evolve as the project grows. Every new pattern is a candidate for a rule or skill. |
| 5 | Claude Code can generate infrastructure code too — but only if CLAUDE.md gives it the right context. |
| 6 | CLAUDE.md is a contract with your future self and future Claude sessions. |
| 7 | The best way to solidify what you learned is to teach it. |

---

*This document is a living record — update it as you complete each phase.*
