#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/') # 'http://www.google.com/'
def home():
    return "Hello world!"

app.run(port=8001)