from flask_sqlalchemy import SQLAlchemy
from decimal import Decimal

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Unicode(128), nullable=False)
    firstname = db.Column(db.Unicode(128))
    lastname = db.Column(db.Unicode(128))
    strava_token = db.Column(db.String(128))
    age = db.Column(db.Integer)
    weight = db.Column(db.Numeric(4, 1))
    max_hr = db.Column(db.Integer)
    rest_hr = db.Column(db.Integer)
    vo2max = db.Column(db.Numeric(4, 2))

    def to_json(self):
        res = {}
        for attr in ('id', 'email', 'firstname', 'lastname', 'age', 'weight',
                     'max_hr', 'rest_hr', 'vo2max', 'strava_token'):
            value = getattr(self, attr)
            if isinstance(value, Decimal):
                value = float(value)
            res[attr] = value
        return res


def new_user(email=None):
    user = User()
    user.email = email if email is not None else 'mario@rossi.it'
    user.firstname = 'mario'
    user.lastname = 'rossi'
    user.age = 23
    user.weight = 70
    user.rest_hr = 60
    user.max_hr = 120
    user.vo2max = 0
    return user
