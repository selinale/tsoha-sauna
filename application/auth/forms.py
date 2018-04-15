from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    confirmation = PasswordField("Password confirmation")
    household = SelectField(
        'Talous',
        choices=[
            ('A1','A1'), ('A2','A2'), ('A3','A3'), ('B4','B4')
        ]
    )

    class Meta:
        csrf = False
    