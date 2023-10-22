#!/usr/bin/python3
"""
script that starts a Flask web application:
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    defining the route
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    defining the route
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    defining the route
    """
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
