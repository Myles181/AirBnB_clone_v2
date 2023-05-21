#!/usr/bin/python3
""" Flask web application """

from flask import Flask, render_template

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

@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>')
def python(text="is_cool"):
    """python page
    Args:
        text -> str() -> default="is cool"
        Return: Python {text}
    """
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def number(n):
    """number page
    Args:
        n -> int()
    Return: n if an integer
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    """number_template
    Args:
        n -> int()
    Return:
        Html page
    """
    return render_template("5-number.html")

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """number_odd_or_even
    Args:
        n -> int()
    Return:
        Html Page
    """
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
