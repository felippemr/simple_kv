from settings import DATABASE_DICT


def handle_put(key, value):
    """Return a tuple containing True and the message
    to send back to the client."""
    DATABASE_DICT[key] = value
    return (True, 'Key [{}] set to [{}]'.format(key, value))
