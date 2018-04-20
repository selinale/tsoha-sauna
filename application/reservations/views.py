from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.reservations.models import Reservation
from application.reservations.forms import ReservationForm


@app.route("/reservations/", methods=["GET"])
def reservations_index():
    return render_template("reservations/list.html")


@app.route("/reservations/new", methods=["POST"])
@login_required(role="ADMIN")
def reservations_create():
    form = ReservationForm(request.form)

    if not form.validate():
        return render_template("reservations/new.html", form=form)

    r = Reservation(form.time.data)
    r.account_id = current_user.id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("reservations_index"))
