# Things to avoid

- Do not call `session.commit()` inside route handlers — commit in the service layer or via
  a dependency that manages the session lifecycle.
- Do not return SQLAlchemy model instances from route handlers — always go through a Pydantic
  schema.
- Do not hardcode the Open-Meteo base URL — put it in config so it can be overridden in tests.
- Do not add `print()` debug statements — use Python's `logging` module.
