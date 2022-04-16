from flask import Blueprint, flash, redirect, render_template, request, url_for

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():

    return render_template("home.html")


@views.route("/game/<int:game_id>/<int:user_id>", methods=["GET", "POST"])
def game():

    return render_template("game.html")


"""
Всё что идёт дальше - бред гения, или просто бред, в зависимости от работоспособности.
НАСТОЯТЕЛЬНО НЕ СОВЕТУЮ ЧТО-ЛИБО МЕНЯТЬ, ибо только я знаю, что в каком костыле используется.
Приятного чтения и поменьше крови из глаз.
"""
