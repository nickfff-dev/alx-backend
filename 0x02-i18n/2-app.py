#!/usr/bin/env python3
""" a get_locale function with the babel.localeselector decorator.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext, lazy_gettext


class Config:
    """Configuration for the Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determine the best locale for the user."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Display the index page."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
