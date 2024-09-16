from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, RadioField, BooleanField, TextAreaField, SelectField, FileField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from .state import state

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "Enter your First Name"})
    middle_name = StringField('Middle Name', render_kw={"placeholder": "Enter your Middle Name"})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Enter your Last Name"})
    email = EmailField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Enter a Password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    occupation = StringField('Occupation', validators=[DataRequired(), Length(max=50)])
    state = SelectField('State', choices=state, validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(max=11)])
    nin = StringField('NIN', validators=[DataRequired(), Length(max=12)])
    marital_status = SelectField('Marital Status', choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced')], validators=[DataRequired()])
    submit = SubmitField('Create Account')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()], render_kw={"placeholder": "Enter your Email Address"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Enter your Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class StaffForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired()])
    occupation = TextAreaField('Occupation', validators=[DataRequired(), Length(max=50)])
    state = SelectField('State', choices=state, validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(max=11)])
    nin = StringField('NIN', validators=[DataRequired(), Length(max=12)])
    marital_status = SelectField('Marital', choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced')], validators=[DataRequired()])
    profile_pic = FileField('Profile Picture')
    submit = SubmitField('Create Account')


class ChildForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name', validators=[DataRequired()])
    profile_pic = FileField('Profile Picture')
    status = SelectField()
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    date_of_birth = DateField('DOB', format='%Y-%m-%d')
    date_admitted = DateField('DOB', format='%Y-%m-%d',  validators=[DataRequired()])
    submit = SubmitField('Submit')