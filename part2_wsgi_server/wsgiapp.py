# self made simple WSGI-app like flask or pyramid or django

def app(envrion, start_respone):
    # starting point of the framework :)

    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_respone(status, response_headers)
    # the 'b' infront (not in the tutorial)
    # encodes the string to byte-string (required in python3)
    return [b'Hello world from a simple WSGI application'] 