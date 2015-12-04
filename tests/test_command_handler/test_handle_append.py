from command_handler import (handle_put, handle_get, handle_delete,
                             handle_append)


def test_handle_append_success():
    key, value = 'TEST', [1, 2, 3, 4]
    handle_put(key, value)
    operation_status, msg = handle_append(key, 5)
    value = handle_get(key)

    assert operation_status is True
    assert msg, "Key [TEST] had value [5] appended"
    assert value[1] == [1, 2, 3, 4, 5]

    handle_delete(key)


def test_handle_append_key_does_not_exists():
    key, value = 'TEST', 5
    operation_status, msg = handle_append(key, value)

    assert operation_status is False
    assert msg == "ERROR: Key [TEST] does not exists"

    handle_delete(key)


def test_handle_append_key_is_not_list():
    key, value = 'TEST', 'ONE'
    handle_put(key, value)
    operation_status, msg = handle_append(key, 1)

    assert operation_status is False
    assert msg == "ERROR: Key [TEST] contains non-list value ([1])"

    handle_delete(key)
