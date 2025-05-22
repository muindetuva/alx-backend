#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """App configs for i18n"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Retrieve user by login_as param"""
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set user context before handling request"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match language from the request
    """
    user = g.get("user")
    if user and user.get("locale") in app.config['LANGUAGES']:
        return user.get("locale")

    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render the index page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
