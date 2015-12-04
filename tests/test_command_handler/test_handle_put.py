from command_handler import (handle_put, handle_get, handle_delete)


def test_handle_put_key_exists():
    key, value = 'TEST', 1
    handle_put(key, value)
    operation_status, p_value = handle_get(key)

    assert operation_status is True
    assert value == p_value

    handle_delete(key)
