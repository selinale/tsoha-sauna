from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class HouseholdForm(FlaskForm):
    id = StringField("Household name", [validators.Length(min=2, max=2)])

    class Meta:
        csrf = False