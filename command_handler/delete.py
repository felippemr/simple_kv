from settings import DATABASE_DICT


def handle_delete(key):
    """Return a tuple containing True if the key could be deleted and
    the message to send back to the client."""
    try:
        del DATABASE_DICT[key]
    except KeyError:
        operation_status = False
        result_msg = 'ERROR: Key [{}] not found and could not be deleted'.format(key)
    else:
        operation_status = True
        result_msg = "Key [{}] deleted".format(key)

    return operation_status, result_msg
