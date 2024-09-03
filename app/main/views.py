from app import app
from flask import render_template
from forms import RegisterForm, LoginForm



@app.route('/', method=['GET', 'POST'], strict_slashes=False)
def index():
    name = None
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.first_name.data
        form.first_name.data = ''
    return render_template('index.html', form=form, name=name)


@app.route("/about_us", strict_lashes=False)
def about_us():
    return


@app.route("/donations", strict_lashes=False)
def donations():
    return



