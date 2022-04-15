# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:16:55 2021

@author: artbo
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import *
from . import db
from .defs import *

views = Blueprint('views', __name__)



@views.route('/', methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note=request.form.get("note")
        if len(note) < 1:
            flash("Напиши хотя-бы один символ, лол", category="error")
        else:
            new_note=Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("какой молодчинка, твоя запись была добавлена)", category="success")

    return render_template("home.html",user=current_user, key=key())


"""
Всё что идёт дальше - бред гения, или просто бред, в зависимости от работоспособности.
НАСТОЯТЕЛЬНО НЕ СОВЕТУЮ ЧТО-ЛИБО МЕНЯТЬ, ибо только я знаю, что в каком костыле используется.
Приятного чтения и поменьше крови из глаз.
"""


@views.route("/posts")
def posts():
    users = User.query.order_by(User.id).all()
    return render_template("posts.html",users=users, user=current_user, key=key())


@views.route("/userpost/<int:noteId>/delete")
def post_del(noteId):
    note=Note.query.get(noteId)
    if note:
        if note.user_id==current_user.id:
            db.session.delete(note)
            db.session.commit()
        else:
            flash("Ты чорт, чо делаешь не в своём аккаунте?", category="error")
    return redirect(url_for("views.home"))


'''
Дальнейшее уже не относится к тесту функционала, теперь только хардкор
теперь только то, что будет использоваться у нас.
'''






'''
А теперь можно добаить другой рендер Resipes при этом сделав путь отрисовки через /vegan_resipes
'''
@views.route("/resipes", methods=["GET","POST"])
def showtime():

    resipes = Resipe.query.order_by(Resipe.id).all()

    ingridients = Ingridient.query.order_by(Ingridient.id).all()
    if request.method=="POST":

        flag_with = request.form.get("Flag_with") == "1"
        flag_reboot = request.form.get("Flag_reboot") == "1"
        flag_exept = request.form.get("Flag_exept") == "1"
        flag_time = request.form.get("Flag_time") == "1"
        flag_amount = request.form.get("Flag_amount") == "1"
        ingr_to_filter = request.form.get("Ingridient_to_sort")



        if flag_reboot:
            success = fitler_resipes_reboot(current_user)
            result_resipes=resipes
            flash("Что-то всё-же произошло", category="success")
#Переделать флаг 1 так, чтобы он добавлял рецепты а не удалял
        if flag_with:
            success = filter_resipes_by_include(current_user, resipes, ingr_to_filter)
            result_resipes = current_user.filter_resipes

        if flag_exept:
            success = filter_resipes_by_delete(current_user, resipes, ingr_to_filter)
            result_resipes = current_user.filter_resipes

        if flag_time:
            result_resipes = Resipe.query.order_by(Resipe.quantity).all()

        if flag_amount:
            result_resipes = Resipe.query.order_by(Resipe.amount).all()


    else:
        result_resipes = resipes


    return render_template("Resipes.html", user=current_user, resipes = resipes, ingridients=ingridients, result_resipes=result_resipes, key=key())



@views.route('/resipe_preview/<int:resipeId>', methods=["GET", "POST"])
def show_resipe_preview(resipeId):
    resipe=Resipe.query.get(resipeId)
    print(resipe.name)
    return render_template("ResipePreview.html", user=current_user, resipe=resipe, key=key())




#ДОБАВИТЬ СЮДА АЙДИШНИК, ЧТОБ ПОД РАЗНЫЕ ТИПЫ ИСПОЛЬЗОВАТЬ ТОЛЬКО ЭТУ ССЫЛКУ
@views.route("/vegan-resipes", methods=["GET", "POST"])
def vegan_resipes():
    dell_ingridients_names = ["мясо","рыба","яйца","молоко"]
    #Добавить IF в выбор ингредиентов

    resipes = Resipe.query.order_by(Resipe.id).all()
    current_user.filter_resipes=[]

    filter_resipes=current_user.filter_resipes
    filter_resipes.clear()

    for res in resipes:
        flag=1
        for ingr in res.ingridients_in_resipe:
            for name_to_dell in dell_ingridients_names:
                if ingr.name ==name_to_dell:
                    flag=0
        if flag:
            filter_resipes.append(res)
    return render_template("VeganResipes.html", user=current_user, resipes = resipes, result_resipes=filter_resipes, key=key())

@views.route("/add_resipes", methods=["GET", "POST"])
def add_resipes():
    '''
    if current_user.id == admin.id:

    else:
    '''
    if request.method=="POST":
        name = request.form.get("name")
        time = request.form.get("time")
        stepbystep = request.form.get("stepbystep")
        quantity = request.form.get("quantity")
        image = request.form.get("image")

        ingridients = str(request.form.get("ingridients")).lower().split()
        amount = len(ingridients)

        '''
        if len(ingridients)<1:
            flash("Ну добавь хоть-один ингредиент!", category="error")

        else:
            for ingr in ingridients:
                check_ingr = Ingridient.query.filter_by(name=ingr).count()
                if check_ingr==0:
                    ingridient = Ingridient(name=ingr)
                    db.session.add(ingridient)
                    db.session.commit()
                    flash("Ты добавил ингридиент!")
        '''

        if time == None:
            time = 20

        if len(name)<2:
            flash("Название короче двух символов? Не смеши)", category="error")

        elif len(stepbystep)<10:
            flash("Гайд не может быть короче 10 символов...", category="error")


        elif image == None:
            flash("Добавь картинку, она обязана быть.", category="error")

        elif len(ingridients)<1:
            flash("Ну добавь хоть-один ингредиент!", category="error")

        else:
            new_resipe = Resipe(
                        name = name,
                        time = time,
                        stepbystep = stepbystep,
                        quantity = quantity,
                        image = image,
                        amount = amount
            )
            db.session.add(new_resipe)
            db.session.commit()
            i=0
            for ingr in ingridients:
                check_ingr = Ingridient.query.filter_by(name=ingr).count()
                if check_ingr==0:
                    ingridient = Ingridient(name=ingr)
                    new_resipe.ingridients_in_resipe.append(ingridient)
                    i+=1
                else:
                    add_ingr = Ingridient.query.filter_by(name=ingr).first()
                    new_resipe.ingridients_in_resipe.append(add_ingr)
                db.session.commit()
            flash("Ты добавил рецепт с"+str(i)+" новыми ингридиентами!")
        #Понять как добавить ингридиенты???????????????????????????????????????? (СДЕЛАНО!)

    return render_template("AddResipes.html", user=current_user, key=key())


@views.route("/resipe_delite/<int:resId>")
def resipe_del(resId):
    user = current_user
    resipe=Resipe.query.get(resId)
    if resipe:
        if user.email==key():
            print(resipe.ingridients_in_resipe)
            resipe.ingridients_in_resipe.clear()
            db.session.commit()
            db.session.delete(resipe)
            db.session.commit()
        else:
            flash("Ты чорт, чо сделать пытаешься? Иди отсюда!", category="error")
    return redirect(url_for("views.showtime"))


@views.route('/add_nirn', methods=["GET", "POST"])
def add_ingridient():
    if request.method=="POST":
        name = request.form.get("name")
        time = request.form.get("time")
        stepbystep = request.form.get("stepbystep")
        quantity = request.form.get("quantity")
        image = request.form.get("image")

        ingridients = str(request.form.get("ingridients")).lower().split()

        '''
        if len(ingridients)<1:
            flash("Ну добавь хоть-один ингредиент!", category="error")

        else:
            for ingr in ingridients:
                check_ingr = Ingridient.query.filter_by(name=ingr).count()
                if check_ingr==0:
                    ingridient = Ingridient(name=ingr)
                    db.session.add(ingridient)
                    db.session.commit()
                    flash("Ты добавил ингридиент!")
        '''

        if time == None:
            time = 20

        if len(name)<2:
            flash("Название короче двух символов? Не смеши)", category="error")

        elif len(stepbystep)<10:
            flash("Гайд не может быть короче 10 символов...", category="error")


        elif image == None:
            flash("Добавь картинку, она обязана быть.", category="error")

        elif len(ingridients)<1:
            flash("Ну добавь хоть-один ингредиент!", category="error")

        else:
            new_nirn = Nirn(
                        name = name,
                        time = time,
                        stepbystep = stepbystep,
                        quantity = quantity,
                        image = image
            )
            db.session.add(new_nirn)
            db.session.commit()
            i=0
            for ingr in ingridients:
                check_ingr = NirnIngridient.query.filter_by(name=ingr).count()
                if check_ingr==0:
                    nirn_ingridient = NirnIngridient(name=ingr)
                    new_nirn.ingridients_in_resipe.append(nirn_ingridient)
                    i+=1
                else:
                    add_ingr = NirnIngridient.query.filter_by(name=ingr).first()
                    new_nirn.ingridients_in_resipe.append(add_ingr)
                db.session.commit()
            flash("Ты добавил рецепт в НИРН с"+str(i)+" новыми ингридиентами!")
        #Понять как добавить ингридиенты???????????????????????????????????????? (СДЕЛАНО!)

    return render_template("AddResipes.html", user=current_user, key=key())



@views.route("/nirn_delite/<int:resId>")
def nirn_del(resId):
    user = current_user
    resipe=Nirn.query.get(resId)
    if resipe:
        if user.email==key():
            print(resipe.ingridients_in_resipe)
            resipe.ingridients_in_resipe.clear()
            db.session.commit()
            db.session.delete(resipe)
            db.session.commit()
        else:
            flash("Ты чорт, чо сделать пытаешься? Иди отсюда!", category="error")
    return redirect(url_for("views.nirn"))



@views.route('/addons_list', methods=["GET", "POST"])
def show_addons_list():
    addons = Addon.query.order_by(Addon.id).all()
    print(addons)
    return render_template("AddonsList.html", user=current_user, addons=addons, key=key())


@views.route("/addon_delite/<int:addonId>")
def addon_del(addonId):
    user = current_user
    addon=Addon.query.get(addonId)
    if addon:
        if user.email==key():
            db.session.delete(addon)
            db.session.commit()
        else:
            flash("Ты чорт, чо сделать пытаешься? Иди отсюда!", category="error")
    return redirect(url_for("views.show_addons_list"))




@views.route('/addon_preview/<int:addonId>', methods=["GET", "POST"])
def show_addon_preview(addonId):
    addon = Addon.query.get(addonId)
    return render_template("AddonPreview.html", user=current_user, addon = addon, key=key())


@views.route('/add_addon', methods=["GET", "POST"])
def add_addon():
    if request.method=="POST":
        name = request.form.get("name")
        what_is_it = request.form.get("what_is_it")

        if len(name)<2:
            flash("Название должно быть длиннее 1 символа!", category="error")
        elif len(what_is_it)<5:
            flash("Описание должно быть длиннее 4 символов!", category="error")
        else:
            new_addon = Addon(name = name,
                          what_is_it = what_is_it)
            db.session.add(new_addon)
            db.session.commit()
            flash("Какая ты молодчинка! Добавка была добавлена!", category="success")

    return render_template("AddAddon.html", user=current_user, key=key())



@views.route('/nirn_preview/<int:nirnId>', methods=["GET", "POST"])
def show_nirn_preview(nirnId):
    resipe=Nirn.query.get(nirnId)
    print(resipe.name)
    return render_template("NirnPreview.html", user=current_user, resipe=resipe, key=key())


@views.route('/nirn', methods=["GET", "POST"])
@login_required
def nirn():
    nirn = Nirn.query.order_by(Nirn.id).all()
    return render_template("Nirn.html", user=current_user, nirn=nirn, key=key())

@views.route("/testgame", methods=["GET", "POST"])
@login_required
def testgame():
    import pygame
    WIDTH_WINDOW, HEIGHT_WINDOW = 1000, 800
    screen = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
    pygame.display.set_caption("Бактерии. Путь к Олимпу")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
    return render_template("home.html", user=current_user, key=key())
