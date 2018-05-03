from datetime import datetime, date

from sqlalchemy.sql import text

from application import db
from application.models import Base


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
        stmt = text("SELECT reservation.hour, account.household "
                    "FROM Reservation "
                    "LEFT JOIN account ON reservation.account_id=account.id "
                    "WHERE date = :reserved ").params(reserved=str(date))

        res = db.engine.execute(stmt)
        res = [(r[0], r[1]) for r in res]


        return res
       
    @staticmethod
    def get_reservations_and_households():
        stmt = text("SELECT account.household, reservation.hour, reservation.date"
                    " FROM account"
                    " LEFT JOIN reservation ON reservation.account_id=account.id")
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            date_row = datetime.strptime(row[2], '%Y-%m-%d') if isinstance(row[2], str) else row[2]

            if date_row == None:
                print("???????", row)
                continue

            response.append({"household":row[0], "hour":row[1], "date": date_row})

        return response                             
