from application import db
from application.models import Base

from sqlalchemy.sql import text

class Reservation(Base):
    date = db.Column(db.Date(), nullable=False)
    hour = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)

    def __init__(self, date, hour):
        self.date = date
        self.hour = hour

    @staticmethod
    def reservation_count():
        stmt = text("SELECT COUNT(Reservation.id)"
                    "FROM Reservation")
        
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def reserved_hours(date):
        stmt = text("SELECT hour "
                    "FROM Reservation "
                    "WHERE date = :reserved").params(reserved=str(date))

        res = db.engine.execute(stmt)
        res = [r[0] for r in res]

        return res             