from fintech_truth_surface_kit import assert_unavailable_is_not_zero


def test_unavailable_portfolio_payload_uses_none() -> None:
    payload = {
        "portfolio_pnl": None,
        "portfolio_value": None,
        "source": "unavailable",
    }

    assert_unavailable_is_not_zero(payload, fields=["portfolio_pnl", "portfolio_value"])
