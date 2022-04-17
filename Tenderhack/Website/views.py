from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from ..Game.game import Test
from . import db
from .models import *

views = Blueprint("views", __name__)

test = Test([], [])


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    # for i in range(10000):
    #    return render_template(
    #        "home.html", user=current_user, graphJSON=test.generate_pict()
    #    )

    if request.method == "POST":
        for i in range(10000):
            test.test_play()
            redirect(url_for("views.home"))

    return render_template(
        "home.html", user=current_user, graphJSON=test.generate_pict()
    )


@views.route("/create_game", methods=["GET", "POST"])
def create_game():
    


@views.route("/game/<int:game_id>/<int:user_id>", methods=["GET", "POST"])
def game():

    return render_template("game.html", user=current_user)


"""
Всё что идёт дальше - бред гения, или просто бред, в зависимости от работоспособности.
НАСТОЯТЕЛЬНО НЕ СОВЕТУЮ ЧТО-ЛИБО МЕНЯТЬ, ибо только я знаю, что в каком костыле используется.
Приятного чтения и поменьше крови из глаз.
"""
