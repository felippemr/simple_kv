from command_handler import (handle_get, handle_put, handle_delete)


def test_handle_get_key_exists():
    key, value = 'TEST', 1
    handle_put(key, value)
    operation_status, p_value = handle_get(key)

    assert operation_status is True
    assert value, p_value

    handle_delete(key)


def test_handle_get_key_does_not_exists():
    key, value = 'TEST', None
    operation_status, p_value = handle_get(key)

    assert operation_status is False
    assert value is p_value
