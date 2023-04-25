#!/usr/bin/env python3
"""0-app module
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """Config object class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get_locale function

    Returns:
        str - locale
    """
    if request.args.get("locale") in app.config['LANGUAGES']:
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """get_user function

    Returns:
        dict - user
    """
    if request.args.get("login_as"):
        return users.get(int(request.args.get("login_as")))
    return None


@app.before_request
def before_request():
    """before_request function
    """
    g.user = get_user()


@app.route("/", methods=["GET"])
def home():
    """index function
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
