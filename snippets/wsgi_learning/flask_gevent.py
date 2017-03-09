from gevent.wsgi import WSGIServer
from flask import Flask
app = Flask(__name__)
@app.route('/')
def main_handler():
    return 'hello word, flask with gevent'

if __name__ == '__main__':
	http_server = WSGIServer(('', 8888), app)
	http_server.serve_forever()