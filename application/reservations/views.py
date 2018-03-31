from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.reservations.models import Reservation
from application.reservations.forms import ReservationForm

@app.route("/reservations/", methods=["GET"])
def reservations_index():
    return render_template("reservations/list.html", reservations = Reservation.query.all())

@app.route("/reservations/new/")
@login_required
def reservations_form():
    return render_template("reservations/new.html", form = ReservationForm())

@app.route("/reservations/<reservation_id>/", methods=["POST"])
@login_required
def reservations_set_done(reservation_id):

    r = Reservation.query.get(reservation_id)
    r.done = True
    db.session().commit()
  
    return redirect(url_for("reservations_index"))    

@app.route("/reservations/", methods=["POST"])
@login_required
def reservations_create():
    form = ReservationForm(request.form)

    if not form.validate():
        return render_template("reservations/new.html", form = form)

    r = Reservation(form.name.data)
    r.done = form.done.data

    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("reservations_index"))