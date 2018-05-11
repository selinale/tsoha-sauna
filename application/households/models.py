from application import db
from application.models import Base

from sqlalchemy.sql import text

class Household(db.Model):

    __tablename__ = "household"

    id = db.Column(db.String, primary_key=True)

    def __init__(self, id):
        self.id = id


            