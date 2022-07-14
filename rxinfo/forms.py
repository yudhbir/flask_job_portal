from flask_wtf import FlaskForm
from wtforms import Form,BooleanField,StringField, PasswordField
from wtforms.validators import DataRequired,InputRequired

class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])