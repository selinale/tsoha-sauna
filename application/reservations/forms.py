from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms import HiddenField

times = [(x, x) for x in range(0, 24)]

class ReservationForm(FlaskForm):
    date = HiddenField("Date")
    hour = SelectField("Time", choices=times)

    class Meta:
        csrf = False