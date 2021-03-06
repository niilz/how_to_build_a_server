#!/usr/bin/env python

# Concurrent server (multiple connections)
# - child process sleeps for 60secs after handling client's request
# - parent and child processes clos duplicat desciptors (file-descriptors)

import os
import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5 # = BACKLOG

def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(
        f'Child PID: {os.getpid()}. Parent PID {os.getppid()}'
    )
    print(request.decode())
    http_response = b"""\
    HTTP/1.1 200 OK

    Hello, World"!
    """
    client_connection.sendall(http_response)
    time.sleep(60)

def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print(f'Serving HTTP on port {PORT} ...')
    print(f'Parent PID (PPID): {os.getpid()}')

    while True:
        client_connection, client_address = listen_socket.accept()
        pid = os.fork() # parent process gets forked (cloned)
        if pid == 0: # child
            listen_socket.close()
            handle_request(client_connection)
            client_connection.close()
            os._exit(0) # child exits here
        else: # parent
            client_connection.close() # close parent copy and loop over

if __name__ == "__main__":
    serve_forever()