from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField


class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")
    confirmation = PasswordField("Salasana uudelleen")
    household = SelectField(
        'Talous',
        choices=[
            ('A1','A1'), ('A2','A2'), ('A3','A3'), ('B4','B4')
        ]
    )

    class Meta:
        csrf = False
    