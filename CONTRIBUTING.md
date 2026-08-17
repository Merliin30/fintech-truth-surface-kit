# Contributing

Contributions are welcome when they keep the project generic, testable, and safe for open-source reuse.

## Development setup

```bash
python -m pip install -e .[dev]
python -m pytest
python -m ruff check .
```

## Contribution rules

- Do not add proprietary platform code.
- Do not add credentials, sample secrets, customer data, or exchange keys.
- Keep helpers small and dependency-free unless a dependency is clearly justified.
- Add tests for every helper or behavior change.
- Prefer explicit unavailable/unknown semantics over silent defaults.

## Pull request checklist

- [ ] Tests pass with `python -m pytest`.
- [ ] Lint passes with `python -m ruff check .`.
- [ ] New behavior is documented.
- [ ] No private data, credentials, or proprietary logic are included.
