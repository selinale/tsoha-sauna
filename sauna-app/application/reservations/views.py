from application import app, db
from flask import redirect, render_template, request, url_for
from application.reservations.models import Reservation

@app.route("/reservations", methods=["GET"])
def reservations_index():
    return render_template("reservations/list.html", reservations = Reservation.query.all())

@app.route("/reservations/new/")
def reservations_form():
    return render_template("reservations/new.html")

@app.route("/reservations/<task_id>/", methods=["POST"])
def reservations_set_done(task_id):

    t = Reservation.query.get(task_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("reservations_index"))    

@app.route("/reservations/", methods=["POST"])
def reservations_create():
    t = Reservation(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("reservations_index"))