#!/usr/bin/env python3
""" Module to  create a Flask app and set up the Babel object."""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


class Config:
    """Configuration for the Flask app."""
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Return a user dictionary or None if the ID cannot be found."""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """Set the current user as a global on flask.g.user."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the best locale for the user."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Display the index page."""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
