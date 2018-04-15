from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class ReservationForm(FlaskForm):
    name = StringField("Reservation name", [validators.Length(min=2)])

    class Meta:
        csrf = False