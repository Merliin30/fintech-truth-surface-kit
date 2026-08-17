from fintech_truth_surface_kit import assert_no_forbidden_truth_markers


def test_production_page_has_no_fixture_markers() -> None:
    rendered_text = "Portfolio unavailable. No substitute values are generated."

    assert_no_forbidden_truth_markers(rendered_text)
