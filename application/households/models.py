from application import db
from application.models import Base

from sqlalchemy.sql import text

class Household(db.Model):

    __tablename__ = "household"

    id = db.Column(db.String, primary_key=True)

    # users = db.relationship("Household", backref='account', lazy=True)

    def __init__(self, id):
        self.id = id
    
    @staticmethod
    def household_count():
        stmt = text("SELECT COUNT(Household.id)"
                    "FROM Household")
        
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

            