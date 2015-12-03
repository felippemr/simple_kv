from parser.exceptions import MissingArgumentException


def parse_message(data):
    try:
        command, key, value, value_type = data.strip().split(';')
    except ValueError:
        raise MissingArgumentException("Wrong number of arguments!")

    try:
        value = {'LIST': value.split(','),
                 'INT': int(value)
                 }.get(value_type, str(value))
    except ValueError:
        value = None

    return command, key, value
