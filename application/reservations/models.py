from application import db
from application.models import Base

from sqlalchemy.sql import text

class Reservation(Base):
    time = db.Column(db.DateTime(), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)

    def __init__(self, time):
        self.time = time

    @staticmethod
    def reservation_count():
        stmt = text("SELECT COUNT(Reservation.id)"
                    "FROM Reservation")
        
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]    