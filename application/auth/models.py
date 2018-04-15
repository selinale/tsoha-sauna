from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    household = db.Column(db.String(2), db.ForeignKey('household.id'))

    reservations = db.relationship("Reservation", backref='account', lazy=True)

    def __init__(self, household, username, password, confirmation):
        self.household = household
        self.username = username
        self.password = password
        self.confirmation = confirmation
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def find_users_with_no_reservations():
        stmt = text("SELECT Account.id, Account.username FROM Account"
                    " LEFT JOIN Reservation ON Reservation.account_id = Account.id"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Reservation.id) = 0")
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"id":row[0], "username":row[1]})   

        return response            