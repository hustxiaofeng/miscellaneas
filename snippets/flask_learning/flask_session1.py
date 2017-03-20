# -*- coding: utf-8 -*-

from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    print session
    return 'hello ' + session['user']

@app.route('/login')
def login():
    session['user'] = 'admin'
    return 'login ok'

if __name__ == '__main__':
    app.run(port=8888, debug=False)