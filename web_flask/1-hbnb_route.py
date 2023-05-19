#!/usr/bin/python3
# Flask web application

from flask import Flask

app = Flask(__name__)
app.strict_slashes=False

@app.route('/')
def home():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)