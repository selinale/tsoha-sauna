from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    confirmation = PasswordField("Password confirmation")
    household = StringField("Household")

    class Meta:
        csrf = False
    