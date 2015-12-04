from command_handler import (handle_putlist, handle_getlist, handle_delete)


def test_handle_get_put_list():
    key, value = 'TEST', [1, 2, 3, 4, 5]
    handle_putlist(key, value)
    operation_status, p_value = handle_getlist(key)

    assert operation_status is True
    assert value, p_value

    handle_delete(key)
