import datetime
from datetime import date

from flask import redirect, render_template, request, url_for
from flask_login import current_user
from sqlalchemy.sql import text

from application import app, db, login_manager, login_required
from application.reservations.forms import ReservationForm
from application.reservations.models import Reservation


@app.route("/reservations/", methods=["GET"])
def reservations_index():
    reservations = Reservation.get_reservations_and_households()
    future_dates = Reservation.get_future_dates()
    count = Reservation.reservation_count()

    dates = []
    for d in future_dates:
        dates.append(d['date'])

    return render_template("reservations/list.html", reservations=reservations, count=count, date=dates)


@app.route("/reservations/new", methods=["POST"])
@login_required()
def reservations_create():
    form = ReservationForm(request.form)
    
    date = datetime.datetime.strptime(form.date.data, "%Y-%m-%d").date()

    r = Reservation(date, form.hour.data)
    r.account_id = current_user.id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("index"))

@app.route("/reservations/delete/<reservation_id>/", methods=["POST"])
@login_required()
def reservations_delete(reservation_id):

    r = Reservation.query.get(reservation_id)
    
    db.session().delete(r)
    db.session().commit()

    return redirect(url_for("reservations_index"))

@app.route("/reservations/edit/<int:reservation_id>", methods=["GET", "POST"])
@login_required()
def reservations_edit(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    date = reservation.date

    if request.method == "GET":
        future_dates = Reservation.get_future_dates()
        available_hours = []

        for day in future_dates:
            if day.get('date') == date:
                available_hours = day.get('hours')

        return render_template("reservations/new.html", form=ReservationForm(), reservation=reservation_id, hours=available_hours)

    form = ReservationForm(request.form)

    r = Reservation.query.get(reservation_id)

    r.date = date
    r.hour = form.hour.data

    db.session().commit()

    return redirect(url_for("index"))
