from settings import DATABASE_DICT


def handle_delete(key):
    """Return a tuple containing True if the key could be deleted and
    the message to send back to the client."""
    if key not in DATABASE_DICT:
        return (
            False,
            'ERROR: Key [{}] not found and could not be deleted'.format(key)
        )
    else:
        del DATABASE_DICT[key]
