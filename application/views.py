import datetime
from datetime import date

from flask import render_template
from flask_login import current_user

from application import app
from application.auth.models import User
from application.reservations.forms import ReservationForm
from application.reservations.models import Reservation


@app.route("/")
def index():
    future_dates = [{'date':date.today() + datetime.timedelta(days=x)} for x in range(0, 13)]

    days_to_string = [
        'Maanantai',
        'Tiistai',
        'Keskiviikko',
        'Torstai',
        'Perjantai',
        'Lauantai',
        'Sunnuntai'
    ]

    for day in future_dates:
        hours = []
        reserved_hours = Reservation.reserved_hours(day['date'])

        for h in range(0, 24):
            if h not in list(map(lambda x: x[0], reserved_hours)):
                hours.append(h)

        day['hours'] = hours
        day['reserved_hours'] = sorted(reserved_hours, key=lambda x: x[0])

    if current_user.is_authenticated:
        my_id = current_user.id
    else:
        my_id = None

    return render_template("index.html", future_dates=future_dates, to_fi=days_to_string, my_id=my_id)
