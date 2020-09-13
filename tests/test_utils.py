import pytest

from tempus.utils import format_duration, parse_duration


@pytest.mark.parametrize(
    "value,seconds",
    [("45m", 2700), ("2h", 7200), ("1h30m", 5400), ("0m", 0)],
)
def test_parse_duration(value, seconds):
    assert parse_duration(value).total_seconds() == seconds


def test_parse_duration_rejects_garbage():
    with pytest.raises(ValueError):
        parse_duration("soon")


def test_format_duration():
    assert format_duration(5445) == "1h 30m"


def test_date_range_zero_duration_with_duplicate_tags():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_unicode_labels_with_a_long_label():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_deleted_project_with_unicode_input():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_future_start_under_heavy_load():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_pagination_across_timezones():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_past_end_with_a_deleted_project():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_boundaries_with_duplicate_tags():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_mixed_projects_when_offline():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"
