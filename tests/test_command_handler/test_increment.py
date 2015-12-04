from command_handler import (handle_put, handle_get, handle_delete,
                             handle_increment)


def test_handle_increment_success():
    key, value = 'TEST', 1
    handle_put(key, value)
    operation_status, msg = handle_increment(key)
    value = handle_get(key)

    assert operation_status is True
    assert msg, "Key [TEST] incremented"
    assert value[1], value + 1

    handle_delete(key)


def test_handle_increment_key_does_not_exists():
    key = 'TEST'
    operation_status, msg = handle_increment(key)

    assert operation_status is False
    assert msg, "ERROR: Key [TEST] does not exists"


def test_handle_increment_key_is_not_int():
    key, value = 'TEST', 'ONE'
    handle_put(key, value)
    operation_status, msg = handle_increment(key)

    assert operation_status is False
    assert msg, "ERROR: Key [TEST] contains non-int value ([ONE])"

    handle_delete(key)
