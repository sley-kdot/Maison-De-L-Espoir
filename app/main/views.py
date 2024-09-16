from .. import app, bootstrap
from flask import render_template, url_for
from app.main.forms import RegisterForm, LoginForm, StaffForm, ChildForm


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.first_name.data
        form.first_name.data = ''
    return render_template('maison/index.html', form=form, name=name)


@app.route("/about_us")
def about_us():
    return "<h1>About Us</h1>"


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    return render_template("auth/register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("auth/login.html", form=form)


@app.route("/donations")
def donations():
    return



