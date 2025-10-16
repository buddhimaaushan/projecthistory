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


def test_duration_timezone_with_large_offsets():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_boundaries_with_unicode_input():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_timezone_for_a_new_account():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_empty_input_across_timezones():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_timezone_with_unicode_input():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_very_long_label_after_a_migration():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_long_running_with_missing_ids():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_long_running_with_a_deleted_project():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_unicode_labels_with_duplicate_tags():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_stale_cache_with_duplicate_tags():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_deleted_project_with_pagination():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_future_start_for_an_archived_project():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_null_project_under_heavy_load():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_sorting_with_null_values():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_past_end_with_unicode_input():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_missing_id_with_large_offsets():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_null_project_with_defaults():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_many_entries_with_a_deleted_project():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_unicode_labels_across_midnight():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_large_values_with_missing_ids():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_unicode_labels_with_defaults():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_pagination_with_missing_ids():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_mixed_projects_with_duplicate_tags():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_duplicates_with_a_deleted_project():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_past_end_under_heavy_load():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_future_start_with_duplicate_tags():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_missing_id_with_pagination():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_long_running_on_an_empty_database():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_sorting_for_an_archived_project():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_partial_data_after_a_migration():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_boundaries_with_large_offsets():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_archived_project_with_a_long_label():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_sorting_after_a_reopen():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_defaults_after_a_migration():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_stale_cache_with_large_offsets():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_deleted_project_across_timezones():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_zero_duration_with_defaults():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_past_end_on_an_empty_database():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_archived_project_with_pagination():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_defaults_under_heavy_load():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_invalid_input_with_mixed_casing():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_sorting_with_mixed_casing():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_missing_id_across_midnight():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_partial_data_after_a_reopen():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_unicode_labels_with_a_deleted_project():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_defaults_with_duplicate_tags():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_boundaries_with_stale_cache():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_sorting_with_pagination():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_duplicates_with_unicode_input():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_future_start_after_a_reopen():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_future_start_with_a_long_label():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_defaults_with_pagination():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_duplicates_across_midnight():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_single_entry_with_missing_ids():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_archived_project_under_heavy_load():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_past_end_with_large_offsets():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_duplicates_with_defaults():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_timezone_with_large_offsets():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_duplicates_with_missing_ids():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_past_end_across_timezones():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_large_values_on_an_empty_database():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_deleted_project_with_mixed_casing():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_very_long_label_on_an_empty_database():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_large_values_with_stale_cache():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_defaults_for_a_new_account():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_partial_data_with_large_offsets():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_unicode_labels_after_a_migration():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_duplicates_across_midnight():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_future_start_for_a_new_account():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_single_entry_with_null_values():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_null_project_with_unicode_input():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_pagination_for_a_new_account():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_null_project_on_an_empty_database():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_null_project_across_timezones():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_duplicates_with_pagination():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_null_project_for_a_new_account():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_unicode_labels_with_missing_ids():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_duplicates_with_duplicate_tags():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_duplicates_with_a_long_label():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_many_entries_with_pagination():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_invalid_input_on_an_empty_database():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_invalid_input_for_a_new_account():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_duplicates_with_null_values():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_partial_data_when_offline():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_boundaries_after_a_reopen():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_defaults_with_a_long_label():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_empty_input_with_null_values():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_defaults_for_an_archived_project():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_defaults_with_large_offsets():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_partial_data_for_a_new_account():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_deleted_project_with_unicode_input():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_unicode_labels_under_heavy_load():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_stale_cache_when_offline():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_unicode_labels_with_pagination():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_unicode_labels_with_large_offsets():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_stale_cache_with_pagination():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_archived_project_with_large_offsets():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_future_start_with_duplicate_tags():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_mixed_projects_with_unicode_input():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_pagination_with_stale_cache():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_large_values_with_pagination():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_partial_data_with_duplicate_tags():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_large_values_across_timezones():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_defaults_under_heavy_load():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_duplicates_with_a_long_label():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_defaults_with_a_deleted_project():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_partial_data_with_mixed_casing():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_null_project_with_a_deleted_project():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_sorting_with_large_offsets():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_invalid_input_for_a_new_account():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_duplicates_with_stale_cache():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_empty_input_for_a_new_account():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_many_entries_across_timezones():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_mixed_projects_with_a_long_label():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_defaults_when_offline():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_duplicates_for_a_new_account():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_single_entry_for_a_new_account():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_past_end_with_defaults():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_duplicates_for_an_archived_project():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_future_start_for_a_new_account():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_pagination_with_large_offsets():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_date_range_mixed_projects_across_timezones():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_empty_input_with_a_long_label():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_date_range_empty_input_with_missing_ids():
    from tempus.utils import parse_date

    with pytest.raises(ValueError):
        parse_date("2021-13-40")


def test_duration_timezone_for_an_archived_project():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_defaults_with_mixed_casing():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_many_entries_with_a_long_label():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"


def test_duration_past_end_with_missing_ids():
    from tempus.utils import format_duration, parse_duration

    assert parse_duration("0m").total_seconds() == 0
    assert format_duration(0) == "0m"
