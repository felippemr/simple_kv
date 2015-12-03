from get import handle_get
from settings import DATABASE_DICT


def handle_increment(key):
    """Return a tuple containing True if the key's value could be incremented
    and the message to send back to the client."""
    return_value = exists, value = handle_get(key)
    if not exists:
        return return_value
    elif not isinstance(value, int):
        return (
            False,
            'ERROR: Key [{}] contains non-int value ([{}])'.format(key, value)
        )
    else:
        DATABASE_DICT[key] = value + 1
        return (True, 'Key [{}] incremented'.format(key))
