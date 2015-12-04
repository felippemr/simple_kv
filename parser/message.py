from parser.exceptions import MissingArgumentException


def parse_message(data):
    try:
        command, key, value, value_type = data.strip().split(';')
    except ValueError:
        raise MissingArgumentException("Wrong number of arguments!")

    if value_type == 'LIST':
        value = value.split(',')
    elif value_type == 'INT':
        value = int(value)
    else:
        value = None

    return command, key, value
