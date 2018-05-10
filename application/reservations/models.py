import datetime
from datetime import date

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
        stmt = text("SELECT reservation.id, account.household, reservation.hour, reservation.date"
                    " FROM account"
                    " LEFT JOIN reservation ON reservation.account_id=account.id")
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            date_row = datetime.datetime.strptime(row[3], '%Y-%m-%d') if isinstance(row[3], str) else row[3]

            if date_row == None:
                continue

            response.append({"id":row[0], "household":row[1], "hour":row[2], "date": date_row})

        return response                         

    @staticmethod
    def get_future_dates():
        future_dates = [{'date':date.today() + datetime.timedelta(days=x)} for x in range(0, 13)]

        for day in future_dates:
            hours = []
            reserved_hours = Reservation.reserved_hours(day['date'])

            for h in range(0, 24):
                if h not in list(map(lambda x: x[0], reserved_hours)):
                    hours.append(h)

            day['hours'] = hours
            day['reserved_hours'] = sorted(reserved_hours, key=lambda x: x[0])
        
        return future_dates

    @staticmethod
    def get_reservations_by_household(household):
        stmt = text("SELECT date, hour, id FROM reservation"
                    " WHERE account_id IN"
                    " (SELECT id FROM account"
                    " WHERE household = :household)"
                    " ORDER BY hour ASC").params(household=str(household))

        res = db.engine.execute(stmt)

        date_dict = {}

        for row in res:
            date = datetime.datetime.strptime(row[0], '%Y-%m-%d').date() if isinstance(row[0], str) else row[0]
            date_key = date.strftime('%d.%m.')

            reservation = "klo {}-{}".format(row[1], row[1]+1)
            date_obj = {"string": reservation, "id": row[2]}

            if date_key in date_dict:
                date_dict[date_key].append(date_obj)
            else:
                date_dict[date_key] = [date_obj]

        return date_dict