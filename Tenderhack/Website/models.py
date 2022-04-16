from flask_login import UserMixin
from sqlalchemy import func

from . import db


class User(db.Model, UserMixin):  # UserMixin для пихания класса User в flask
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
