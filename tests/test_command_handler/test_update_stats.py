from command_handler import (update_stats, handle_stats)
from settings import STATS_DICT


def test_update_stats_true():
    command, operation_status = 'PUT', True
    update_stats(command, operation_status)

    result = handle_stats()
    assert result[0] is True
    assert result[1]['PUT']['success'] == 1
    assert result[1]['PUT']['error'] == 0

    STATS_DICT['PUT']['success'] = 0


def test_update_stats_false():
    command, operation_status = 'PUT', False
    update_stats(command, operation_status)

    result = handle_stats()
    assert result[0] is True
    assert result[1]['PUT']['error'] == 1
    assert result[1]['PUT']['success'] == 0

    STATS_DICT['PUT']['error'] = 0
