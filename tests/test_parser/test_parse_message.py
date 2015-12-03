import pytest
from parser import parse_message
from parser.exceptions import MissingArgumentException


def test_parse_message_success():
    command = 'PUT'
    key = 'TEST'
    value = 1
    value_type = 'INT'
    good_data = '{};{};{};{}'.format(command, key, value, value_type)
    p_command, p_key, p_value = parse_message(good_data)

    assert command, p_command
    assert key, p_key
    assert value, p_value


def test_parse_message_with_missing_argument():
    with pytest.raises(MissingArgumentException) as excinfo:
        command = 'PUT'
        key = 'TEST'
        value = 1
        bad_data = '{};{};{}'.format(command, key, value)
        p_command, p_key, p_value = parse_message(bad_data)

    assert 'Wrong number of arguments!', str(excinfo.value)
