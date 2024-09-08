from wtforms import StringField, validators, PasswordField, SubmitField, FileField
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[validators.DataRequired(), validators.Length(min=3)])
    last_name = StringField("Last Name", validators=[validators.DataRequired(), validators.Length(min=3)])
    email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=8)])
    submit = SubmitField("Register")