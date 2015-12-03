from get import handle_get


def handle_getlist(key):
    """Return a tuple containing True if the key contained a list and
    the message to send back to the client."""
    return_value = exists, value = handle_get(key)
    if not isinstance(value, list):
        return (
            False,
            'ERROR: Key [{}] contains non-list value ([{}])'.format(key, value)
        )
    else:
        return return_value
