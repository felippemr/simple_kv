from settings import DATABASE_DICT


def handle_get(key):
    """Return a tuple containing True if the key exists and the message
    to send back to the client."""
    try:
        return_value = DATABASE_DICT[key]
        operation_status = True
    except KeyError:
        operation_status = False
        return_value = None
    return (operation_status, return_value)
