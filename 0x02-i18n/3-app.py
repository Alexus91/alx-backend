#!/usr/bin/env python3
""" Flask webapp """
from flask import Flask, render_template, request
from flask_babel import Babel, _
import os

class Config(object):
    """Configu Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Select a language translation to use based on user preferences."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index():
    """Handles / route"""
    return render_template('3-index.html')

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)

