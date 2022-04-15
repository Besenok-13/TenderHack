from flask import request
from flask_login import current_user

from . import db
from .models import *


def key():
    return "artbondar2003@gmail.com"


def filter_resipes_by_include(user, resipes, ingridient):

    resipes_to_filter = user.filter_resipes

    if resipes_to_filter == []:
        for resipe in resipes:
            resipes_to_filter.append(resipe)
        db.session.commit()

    flag_was_filter = 0
    for res in resipes_to_filter:

        if not is_ing_in_resipe(res, ingridient):
            # посмотреть, возможно ли это запихнуть в список, чтобы в последствии
            # за один раз взть и удалить все рецепты, не вызывая коммит
            user.filter_resipes.remove(res)
            flag_was_filter = 1
    db.session.commit()

    return flag_was_filter


def filter_resipes_by_delete(user, resipes, ingridient):
    resipes_to_filter = user.filter_resipes

    if resipes_to_filter == []:
        for resipe in resipes:
            resipes_to_filter.append(resipe)
        db.session.commit()

    flag_was_filter = 0
    for res in resipes_to_filter:

        if is_ing_in_resipe(res, ingridient):
            # посмотреть, возможно ли это запихнуть в список, чтобы в последствии
            # за один раз взть и удалить все рецепты, не вызывая коммит
            user.filter_resipes.remove(res)
            flag_was_filter = 1
    db.session.commit()

    return flag_was_filter


def is_ing_in_resipe(resipe, ingridient):
    flag = False
    for ingr in resipe.ingridients_in_resipe:
        print("Проверили")
        if ingr.name == ingridient:
            flag = True
            print("СОВПАЛО!!!!!!!!!!!!!")

    return flag


def fitler_resipes_reboot(user):
    user.filter_resipes.clear()
    db.session.commit()
    return True


"""
        if flag1=="1":
            current_user.filter_resipes.clear()
            flash("Была произведена очистка!", category="error")

        filter_resipes=current_user.filter_resipes
        name = request.form.get("Ingridient_to_sort")
        print(filter_resipes)
        print(name)

        if filter_resipes!=[]:
            for resipe in filter_resipes:
                delit_or_not_delit=flag2
                for ingr in resipe.ingridients_in_resipe:

                    if ingr.name==name:
                        delit_or_not_delit= not flag2

                if delit_or_not_delit:
                    filter_resipes.remove(resipe)
                    db.session.commit()
                    flash("Фильтр прошёл успешно, удалили"+resipe.name, category="success")


        else:
            for resipe in resipes:
                twins_del=1
                addictive=1
                for ingr in resipe.ingridients_in_resipe:
                    if flag2:
                        if ingr.name==name and twins_del:
                            filter_resipes.append(resipe)
                            db.session.commit()
                            twins_del=0
                            flash("Фильтр прошёл успешно, добавили"+resipe.name, category="success")
                    else:
                        if ingr.name==name and twins_del:
                            addictive=0
                            twins_del=0
                if addictive and (not flag2):
                    filter_resipes.append(resipe)
                    db.session.commit()
                    flash("Фильтр прошёл успешно!!!!!!!!!!!, добавили"+resipe.name, category="error")


    else:
        filter_resipes=resipes
        """
