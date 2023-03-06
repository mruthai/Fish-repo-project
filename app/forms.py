from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, EqualTo

#register form
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match")])
    submit = SubmitField('Register')

#login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me Please')
    submit = SubmitField('Login')

#livestock form
class LivestockForm(FlaskForm):
    classifications = StringField('Classifications', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired()])
    breed = StringField('Breed', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Submit')

#search from
class SearchForm(FlaskForm):
    search = StringField('Search name of Animal', validators=[DataRequired()])
    submit = SubmitField('Search')