#!/usr/bin/env python3
"""flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False


class Config:
    """Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """
    language match based on supported languages
    """
    language_available = app.config['LANGUAGES']
    return request.accept_languages.best_match(language_available)

@app.route("/")
def index_1() -> str:
    """ route """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()