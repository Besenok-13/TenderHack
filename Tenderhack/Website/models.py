from flask_login import UserMixin
from sqlalchemy import func

from . import db

Kots_Users = db.Table(
    "favorite_user_resipes",
    db.Column("User_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("Kot_id", db.Integer, db.ForeignKey("kot.id")),
)


class User(db.Model, UserMixin):  # UserMixin для пихания класса User в flask
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    kots = db.relationship("Kot", secondary=Kots_Users, backref="kots")
    first = db.Column(db.Boolean)


class Kot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #   user.id пишется с маленькой буквы, так как мы используем db.ForeignKey а в нём в названии класса большие буквы превращаются в маленькие
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    participaints = db.relationship(
        "User", secondary=Kots_Users, backref="participaints"
    )

