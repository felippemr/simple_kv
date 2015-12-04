from command_handler import (handle_stats)


def test_handle_stats():
    operation_status, stats_dict = handle_stats()

    assert operation_status is True
    assert type(stats_dict) == dict
