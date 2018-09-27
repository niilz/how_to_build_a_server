#!/usr/bin/env python

"""
following the "let's build a server"-tutorial on
https://ruslanspivak.com/lsbaws-part1/
by Rulans Spivak
"""

import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f'Serving HTTP on Port {PORT}')

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(f'{client_address} has requested')
    

    http_response = """\
    HTTP/1.1 200 OK

    Hello, World!
    """
    # .encode() is not in the tutorial but it's necessary for python3
    # because byte transfer is required (string won't work)
    client_connection.sendall(http_response.encode())
    client_connection.close()