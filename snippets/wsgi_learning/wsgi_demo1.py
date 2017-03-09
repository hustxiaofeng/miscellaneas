from wsgiref.simple_server import make_server


def app(environ, start_response):
    start_response('200 Ok', [('Content-Type', 'text/plain')])
    return ['Hello World wsgiref!']


if __name__ == '__main__':
    server = make_server('127.0.0.1', 8080, app)
    print 'Server start at 127.0.0.1:8080...'
    server.serve_forever()