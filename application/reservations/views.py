import datetime

from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.reservations.forms import ReservationForm
from application.reservations.models import Reservation


@app.route("/reservations/", methods=["GET"])
def reservations_index():
    reservations = Reservation.query.all()
    count = Reservation.reservation_count()
    return render_template("reservations/list.html", reservations=reservations, count=count)


@app.route("/reservations/new", methods=["POST"])
@login_required()
def reservations_create():
    form = ReservationForm(request.form)
    
    date = datetime.datetime.strptime(form.date.data, "%Y-%m-%d").date()

    r = Reservation(date, form.hour.data)
    r.account_id = current_user.id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("reservations_index"))
