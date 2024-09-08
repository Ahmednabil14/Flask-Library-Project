from wtforms import StringField, validators, PasswordField, SubmitField
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators=[validators.DataRequired()])
    login = SubmitField("Login")