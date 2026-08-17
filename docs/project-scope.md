# Project scope

FinTech Truth Surface Kit is a generic open-source testing toolkit for financial and trading-adjacent applications.

The project focuses on reusable release-gate checks for customer-facing truth surfaces:

- fixture and demo leakage
- unavailable values rendered as zero
- tier authority drift
- unsafe execution-adjacent tests
- misleading production status or provenance

## In scope

- Small dependency-free Python guard helpers.
- Pytest examples.
- CI-ready test patterns.
- Documentation for common truth-surface failure modes.

## Out of scope

- Trading strategies.
- Exchange connectivity.
- Brokerage, custody, execution, or investment functionality.
- Product-specific private code.
- Customer data, credentials, or API keys.

## Design principles

- Fail closed on unsafe ambiguity.
- Preserve real zero as data, but never use zero as an unavailable fallback.
- Treat server-side authority as canonical for customer tier and entitlement checks.
- Keep tests portable across financial dashboards, trading dashboards, and portfolio applications.
