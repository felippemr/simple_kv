from get import handle_get
from settings import DATABASE_DICT


def handle_increment(key):
    """Return a tuple containing True if the key's value could be incremented
    and the message to send back to the client."""
    exists, value = handle_get(key)

    try:
        DATABASE_DICT[key]
        DATABASE_DICT[key] = value + 1
    except KeyError:
        operation_status = False
        return_msg = 'ERROR: Key [{}] does not exists'.format(key)
    except TypeError:
        operation_status = False
        return_msg = 'ERROR: Key [{}] contains non-int value ([{}])'.format(key, value)
    else:
        operation_status = True
        return_msg = 'Key [{}] incremented'.format(key)

    return operation_status, return_msg
