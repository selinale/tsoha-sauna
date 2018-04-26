from flask import render_template
from application import app
from application.auth.models import User

from datetime import date
import datetime

from application.reservations.forms import ReservationForm

@app.route("/")
def index():
    future_dates = [date.today() + datetime.timedelta(days=x) for x in range(0, 13)]

    days_to_string = [
        'maanantai',
        'tiistai',
        'keskiviikko',
        'torstai',
        'perjantai',
        'lauantai',
        'sunnuntai'
    ]
    
    return render_template("index.html", future_dates=future_dates, to_fi=days_to_string)
