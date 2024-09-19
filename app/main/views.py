from .. import app, db, bootstrap, bcrypt
from flask import render_template, url_for, redirect, flash, get_flashed_messages
from app.main.forms import RegisterForm, LoginForm, StaffForm, ChildForm
from app.models import User, Staff

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('maison/index.html')


@app.route("/about_us")
def about_us():
    return "<h1>About Us</h1>"


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(first_name=form.first_name.data, middle_name=form.middle_name.data,
                    last_name=form.last_name.data, email=form.email.data,
                    password=hashed_pwd, gender=form.gender.data,
                    address=form.address.data, occupation=form.occupation.data,
                    state=form.state.data, phone_num=form.phone.data,
                    nin=form.nin.data, marital_status=form.marital_status.data,
                    )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.last_name.data}, {form.first_name.data}!", "success")
        return redirect(url_for("login"))
    print(get_flashed_messages())
    return render_template("auth/register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("auth/login.html", form=form)


@app.route("/donations")
def donations():
    return



