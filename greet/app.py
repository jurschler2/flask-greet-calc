from flask import Flask

app = Flask(__name__)


@app.route("/welcome")
def welcome_message():
    """Docstring"""

    return "welcome"


@app.route("/welcome/home")
def welcome_home():
    """Docstring"""

    return "welcome home"


@app.route("/welcome/back")
def welcome_back():
    """Docstring"""

    return "welcome back"
