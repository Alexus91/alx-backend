#!/usr/bin/env python3
"""fask web app"""
from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)

app.url_map.strict_slashes = False


class Config:
    """Represents a Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route("/")
def index_6() -> str:
    """The index function displays the home pagen """
    return render_template("6-index.html")


@babel.localeselector
def get_locale() -> str:
    """ Determines the best match for the client  """

    locale = request.args.get('locale')
    supported_languages = app.config["LANGUAGES"]
    if locale and locale in supported_languages:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Union[Dict, None]:
    """Returns a user dictionary based on the id """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Function to be executed before every request."""
    user = get_user()
    g.user = user


app.before_request(before_request)


if __name__ == "__main__":
    app.run(debug=True)
