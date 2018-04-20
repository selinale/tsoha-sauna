from flask_wtf import FlaskForm
from wtforms_components import SelectField

times = [(x, x) for x in range(0, 24)]

class ReservationForm(FlaskForm):
    time = SelectField("Time", choices=times)

    class Meta:
        csrf = False