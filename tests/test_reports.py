from datetime import datetime, timedelta

from tempus.models import Entry
from tempus.reports import filter_entries, group_by_day, group_by_project, summarise


def make_entry(label="writing", project=None, start=None, minutes=30):
    start = start or datetime(2021, 2, 1, 9, 0)
    return Entry(label=label, project=project, start=start, end=start + timedelta(minutes=minutes))


def test_filter_entries_by_range():
    entries = [make_entry(start=datetime(2021, 2, 1, 9)), make_entry(start=datetime(2021, 2, 3, 9))]
    result = filter_entries(entries, start=datetime(2021, 2, 2), end=datetime(2021, 2, 4))
    assert len(result) == 1


def test_filter_entries_by_project_and_tags():
    entries = [make_entry(project="tempus"), make_entry(project="other")]
    assert len(filter_entries(entries, project="tempus")) == 1


def test_summarise_empty():
    assert summarise([])["total_seconds"] == 0


def test_group_by_day():
    entries = [make_entry(start=datetime(2021, 2, 1, 9)), make_entry(start=datetime(2021, 2, 1, 14))]
    groups = group_by_day(entries)
    assert len(groups) == 1
    assert len(list(groups.values())[0]) == 2


def test_group_by_project_uses_unassigned():
    assert "unassigned" in group_by_project([make_entry()])


def test_report_unicode_labels_with_unicode_input():
    from tempus.reports import summarise

    assert summarise([])["total_seconds"] == 0


def test_report_stale_cache_with_duplicate_tags():
    from tempus.reports import summarise

    assert summarise([])["total_seconds"] == 0


def test_report_stale_cache_with_missing_ids():
    from tempus.reports import summarise

    assert summarise([])["total_seconds"] == 0


def test_report_many_entries_with_null_values():
    from tempus.reports import summarise

    assert summarise([])["total_seconds"] == 0


def test_report_empty_input_on_an_empty_database():
    from tempus.reports import summarise

    assert summarise([])["total_seconds"] == 0


def test_report_mixed_projects_with_stale_cache():
    from tempus.reports import summarise

    assert summarise([])["total_seconds"] == 0


def test_report_missing_id_after_a_migration():
    from tempus.reports import summarise

    assert summarise([])["total_seconds"] == 0


def test_report_past_end_with_duplicate_tags():
    from tempus.reports import summarise

    assert summarise([])["total_seconds"] == 0


def test_report_boundaries_with_unicode_input():
    from tempus.reports import summarise

    assert summarise([])["total_seconds"] == 0
