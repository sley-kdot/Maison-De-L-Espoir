from .. import app
from flask import render_template
from app.main.forms import RegisterForm, LoginForm




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


@app.route("/register")
def register():
    form = RegisterForm()
    return 


@app.route("/login")
def login():
    form = LoginForm()
    return


@app.route("/donations")
def donations():
    return



