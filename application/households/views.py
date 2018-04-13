from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.households.models import Household
from application.households.forms import HouseholdForm

@app.route("/households", methods = ['GET'])
def list_households():
    households = Household.query.all()
    count = Household.household_count()

    return render_template('households/list.html', households=households, count=count)


@app.route("/households/new/")
@login_required
def households_form():
    return render_template("households/new.html", form=HouseholdForm())

@app.route("/households", methods = ['POST'])
@login_required
def households_create():
    form = HouseholdForm(request.form)

    if not form.validate():
        return render_template("households/new.html", form=form)

    r = Household(form.id.data)

    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("list_households"))
