from flask_wtf import FlaskForm
from wtforms import Form,BooleanField,StringField, PasswordField
from wtforms.validators import DataRequired,InputRequired,Email

class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])

class PatientForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(),Email()])
    date_of_birth = StringField('Date Birth', validators=[InputRequired()])
    gender = StringField('Gender', validators=[InputRequired()])
    age = StringField('Age', validators=[InputRequired()])