from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from ..Game.game import generate_pict
from . import db
from .models import *

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():

    return render_template("home.html", user=current_user, graphJSON=generate_pict())


@views.route("/game/<int:game_id>/<int:user_id>", methods=["GET", "POST"])
def game():

    return render_template("game.html", user=current_user)


"""
Всё что идёт дальше - бред гения, или просто бред, в зависимости от работоспособности.
НАСТОЯТЕЛЬНО НЕ СОВЕТУЮ ЧТО-ЛИБО МЕНЯТЬ, ибо только я знаю, что в каком костыле используется.
Приятного чтения и поменьше крови из глаз.
"""
