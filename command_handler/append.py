from get import handle_get
from settings import DATABASE_DICT


def handle_append(key, value):
    """Return a tuple containing True if the key's value could be appended to
    and the message to send back to the client."""
    exists, list_value = handle_get(key)

    try:
        DATABASE_DICT[key]
        DATABASE_DICT[key].append(value)
    except KeyError:
        operation_status = False
        return_msg = 'Key [{}] does not exists'.format(key)
    except AttributeError:
        operation_status = False
        return_msg = 'ERROR: Key [{}] contains non-list value ([{}])'.format(key, value)
    else:
        operation_status = True
        return_msg = 'Key [{}] had value [{}] appended'.format(key, value)

    return operation_status, return_msg
