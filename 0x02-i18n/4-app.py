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


@app.route("/", methods=["GET"])
def home():
    """index function
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
