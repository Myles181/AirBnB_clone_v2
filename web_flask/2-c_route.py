#!/usr/bin/python3
""" Flask web application """

from flask import Flask

app = Flask(__name__)
app.strict_slashes=False

@app.route('/')
def home():
    """ Home page
    Return: Hello HBNB!
    """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """ HBNB page
    Return: HBNB
    """
    return "HBNB"

@app.route('/c/<text>')
def c(text):
    """ C page
    Args:
        text -> str()
    Return: C {text}
    """
    return "C {}".format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
