"""Guard helpers for customer-facing financial truth surfaces.

The helpers are deliberately small and dependency-free so projects can use them in
pytest suites, smoke tests, or release gates.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any


class TruthSurfaceError(AssertionError):
    """Raised when a truth-surface contract is violated."""


def assert_no_forbidden_truth_markers(
    rendered_text: str,
    *,
    forbidden_markers: Iterable[str] | None = None,
) -> None:
    """Fail if production-rendered text contains known demo/fixture markers."""

    markers = tuple(
        forbidden_markers
        or (
            "static demo",
            "fixture",
            "mock data",
            "sample pnl",
            "placeholder pnl",
            "synthetic portfolio",
        )
    )
    lower_text = rendered_text.lower()
    found = [marker for marker in markers if marker.lower() in lower_text]
    if found:
        raise TruthSurfaceError(f"Forbidden production truth markers found: {found}")


def assert_unavailable_is_not_zero(payload: Mapping[str, Any], *, fields: Iterable[str]) -> None:
    """Fail when unavailable fields are represented as numeric zero.

    A real zero is valid only when the upstream source explicitly measured zero.
    Missing or unavailable values should be represented as None or an explicit
    unavailable envelope, not as 0.
    """

    violations: list[str] = []
    for field in fields:
        value = payload.get(field)
        if value == 0 or value == 0.0 or value == "0":
            violations.append(field)
    if violations:
        raise TruthSurfaceError(
            "Unavailable fields must not be encoded as zero: " + ", ".join(violations)
        )


def assert_tier_authority(
    *,
    server_tier: str,
    effective_tier: str,
    query_tier: str | None = None,
    cookie_tier: str | None = None,
) -> None:
    """Fail if URL or writable-cookie tier data overrides server authority."""

    if effective_tier != server_tier:
        raise TruthSurfaceError(
            f"Effective tier {effective_tier!r} does not match server tier {server_tier!r}"
        )
    if query_tier and query_tier != server_tier and effective_tier == query_tier:
        raise TruthSurfaceError("Query tier was incorrectly accepted as authority")
    if cookie_tier and cookie_tier != server_tier and effective_tier == cookie_tier:
        raise TruthSurfaceError("Writable cookie tier was incorrectly accepted as authority")


def assert_no_live_execution_without_authorization(
    *,
    runtime_mode: str,
    execution_mode: str,
    authorization_token: str | None,
    required_token: str = "YES_I_UNDERSTAND_LIVE_OR_PAPER_EXECUTION",
) -> None:
    """Fail closed when a test can touch live or paper execution without explicit consent."""

    risky_runtime = runtime_mode.upper() in {"LIVE", "PAPER"}
    risky_execution = execution_mode.upper() not in {"OFF", "LAB", "SIMULATION"}
    if risky_runtime and risky_execution and authorization_token != required_token:
        raise TruthSurfaceError(
            "Execution-adjacent test requires explicit authorization before proceeding"
        )
