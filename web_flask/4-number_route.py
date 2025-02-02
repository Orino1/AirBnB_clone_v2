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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is_cool"):
    """
    defining the route
    """
    formatted_text = text.replace('_', ' ')
    return 'Python {}'.format(formatted_text)


@app.route('/number/<n>', strict_slashes=False)
def number_n(n):
    """
    defining the route
    """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
