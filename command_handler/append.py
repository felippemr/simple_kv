from get import handle_get
from settings import DATABASE_DICT


def handle_append(key, value):
    """Return a tuple containing True if the key's value could be appended to
    and the message to send back to the client."""
    return_value = exists, list_value = handle_get(key)
    if not exists:
        return return_value
    elif not isinstance(list_value, list):
        return (
            False,
            'ERROR: Key [{}] contains non-list value ([{}])'.format(key, value)
        )
    else:
        DATABASE_DICT[key].append(value)
        return (True, 'Key [{}] had value [{}] appended'.format(key, value))
