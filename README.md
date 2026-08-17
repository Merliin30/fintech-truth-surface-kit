# FinTech Truth Surface Kit

Open-source test utilities and governance patterns for financial applications that need to keep customer-facing truth surfaces honest.

This project helps maintainers test that production financial dashboards do not accidentally render:

- demo or fixture data as production truth
- synthetic profit and loss values
- query or cookie based tier spoofing
- unavailable data as zero, neutral, or healthy
- live-execution paths inside tests without explicit authorization

The project is intentionally generic. It does not include proprietary trading strategies, private platform code, credentials, customer data, exchange keys, or financial advice.

## Why this exists

Financial and trading applications often have several layers between source data and the UI: execution engines, event streams, read models, APIs, server rendering, and browser components. Bugs at those boundaries can make a customer see values that look authoritative but are actually placeholders, fixtures, stale data, or unsafe defaults.

This kit provides reusable checks for those boundaries.

## Included checks

- `assert_no_forbidden_truth_markers`: fail if production output contains forbidden fixture/demo/static markers.
- `assert_unavailable_is_not_zero`: fail if unavailable fields are silently rendered as `0`.
- `assert_tier_authority`: verify that user tier comes from server authority, not URL parameters or writable cookies.
- `assert_no_live_execution_without_authorization`: fail closed unless a test explicitly authorizes paper/live-adjacent execution.

## Example use cases

- API contract tests that prevent unavailable financial fields from becoming `0`.
- Browser smoke tests that fail when production pages contain fixture or demo markers.
- Auth tests that prove query strings and writable cookies cannot elevate a customer's tier.
- CI release gates that block live or paper-execution tests unless explicit authorization is present.

## Installation

```bash
pip install fintech-truth-surface-kit
```

For local development:

```bash
pip install -e .[dev]
pytest
```

## Minimal example

```python
from fintech_truth_surface_kit import assert_unavailable_is_not_zero

payload = {"portfolio_pnl": None, "source": "unavailable"}
assert_unavailable_is_not_zero(payload, fields=["portfolio_pnl"])
```

## Security and scope

This repository contains generic safety patterns only. It does not execute trades, connect to exchanges, store secrets, or provide financial advice. See `SECURITY.md` for vulnerability reporting.

## Roadmap

See `ROADMAP.md` for planned helpers and examples.

## License

MIT License.
