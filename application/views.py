from flask import render_template
from application import app
from application.auth.models import User

from datetime import date
import datetime

from application.reservations.forms import ReservationForm
from application.reservations.models import Reservation

@app.route("/")
def index():
    future_dates = [date.today() + datetime.timedelta(days=x) for x in range(0, 13)]

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
        hours = Reservation.reserved_hours(day)
        print(hours)

    return render_template("index.html", future_dates=future_dates, to_fi=days_to_string)

    
