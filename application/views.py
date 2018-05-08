
from flask import render_template
from flask_login import current_user

from application import app
from application.auth.models import User
from application.reservations.forms import ReservationForm
from application.reservations.models import Reservation


@app.route("/")
def index():
    days_to_string = [
        'Maanantai',
        'Tiistai',
        'Keskiviikko',
        'Torstai',
        'Perjantai',
        'Lauantai',
        'Sunnuntai'
    ]

    if current_user.is_authenticated:
        my_id = current_user.id
    else:
        my_id = None

    future_dates = Reservation.get_future_dates()

    return render_template("index.html", future_dates=future_dates, to_fi=days_to_string, my_id=my_id)
