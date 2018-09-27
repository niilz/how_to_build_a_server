#!/usr/bin/env python

# iterative server - webserver3a.py
# with SLEEP inbetween for 60seconds after sending a response to a client

import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5

def handle_request(client_connection):
    request = client_connection.recv(1024)
    http_response = b"""\
    HTTP/1.1 200OK

    Hello, World!
    """
    client_connection.sendall(http_response)
    time.sleep(60) # sleep and block the process for 60secs

def serve_forever():
    # create a socket
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # make sure the adress is kept after the request
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # with TCP "bind" can take port-no., IP-adress, both or neither (here: address)
    listen_socket.bind(SERVER_ADDRESS)
    # make socket a listening-socket
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print(f'Serving HTTP on port {PORT} ...')

    while True:
        # tells the kernel to accept incoming connection requests
        client_connection, client_address = listen_socket.accept()
        # read data and print it to standard-output
        handle_request(client_connection)
        # close connection for next request
        client_connection.close()

if __name__ == "__main__":
    serve_forever()