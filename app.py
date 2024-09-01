from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "<h1>MAISON DE L'ESPOIR<h1>"


@app.route("/about_us", strict_lashes=False)
def about_us():
    return


@app.route("/donations", strict_lashes=False)
def donations():
    return



