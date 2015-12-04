from command_handler import (handle_put, handle_delete)


def test_handle_delete_key_exists():
    key, value = 'TEST', 1
    handle_put(key, value)
    operation_status, msg = handle_delete(key)

    assert operation_status is True
    assert msg == "Key [TEST] deleted"


def test_handle_delete_key_does_not_exists():
    key = 'TEST'
    operation_status, msg = handle_delete(key)

    assert operation_status is False
    assert msg == "ERROR: Key [TEST] not found and could not be deleted"
