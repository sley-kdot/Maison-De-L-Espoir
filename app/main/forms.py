from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name')
    email = EmailField('Email', validators=[DataRequired(), Email()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    gender = RadioField()
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')