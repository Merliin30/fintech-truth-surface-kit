import pytest

from fintech_truth_surface_kit import (
    TruthSurfaceError,
    assert_no_forbidden_truth_markers,
    assert_no_live_execution_without_authorization,
    assert_tier_authority,
    assert_unavailable_is_not_zero,
)


def test_forbidden_truth_markers_fail() -> None:
    with pytest.raises(TruthSurfaceError):
        assert_no_forbidden_truth_markers("Portfolio: static demo PnL")


def test_unavailable_zero_fails() -> None:
    with pytest.raises(TruthSurfaceError):
        assert_unavailable_is_not_zero({"pnl": "0"}, fields=["pnl"])


def test_none_unavailable_passes() -> None:
    assert_unavailable_is_not_zero({"pnl": None}, fields=["pnl"])


def test_tier_authority_uses_server_tier() -> None:
    assert_tier_authority(
        server_tier="pro",
        query_tier="vip",
        cookie_tier="vip",
        effective_tier="pro",
    )


def test_query_tier_cannot_elevate() -> None:
    with pytest.raises(TruthSurfaceError):
        assert_tier_authority(server_tier="free", query_tier="vip", effective_tier="vip")


def test_execution_requires_authorization() -> None:
    with pytest.raises(TruthSurfaceError):
        assert_no_live_execution_without_authorization(
            runtime_mode="PAPER",
            execution_mode="FREQTRADE",
            authorization_token=None,
        )
