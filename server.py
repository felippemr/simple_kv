import socket
import sys
from settings import (HOST, PORT, logging)
from command_handler import COMMAND_HANDLERS
from parser import parse_message
from parser.exceptions import MissingArgumentException

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def exit_gracefully(*args):
    logging.info("Shutting down...")
    sys.exit(0)


def main():
    SOCKET.bind((HOST, PORT))
    SOCKET.listen(1)

    while True:
        try:
            connection, address = SOCKET.accept()
        except KeyboardInterrupt:
            exit_gracefully()

        logging.info('New connection from [{}]'.format(address))
        try:
            data = connection.recv(4096).decode()
            command, key, value = parse_message(data)

            if command == 'STATS':
                response = COMMAND_HANDLERS['STATS']()
            elif command in (
                'GET',
                'GETLIST',
                'INCREMENT',
                'DELETE'
            ):
                response = COMMAND_HANDLERS[command](key)
            elif command in (
                'PUT',
                'PUTLIST',
                'APPEND',
            ):
                response = COMMAND_HANDLERS[command](key, value)
            else:
                response = (False, 'Unknown command type [{}]'.format(command))
            COMMAND_HANDLERS['UPDATE_STATS'](command, response[0])
        except MissingArgumentException as e:
            connection.sendall('False;{}'.format(e))
        finally:
            if 'response' in locals():
                connection.sendall('{};{}'.format(response[0], response[1]))
            connection.close()

if __name__ == '__main__':
    main()
