#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """App configs for i18n"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match language from the request
    """
    locale = request.args.get('locale')
    print("Selected locale:", locale)
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render the index page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
