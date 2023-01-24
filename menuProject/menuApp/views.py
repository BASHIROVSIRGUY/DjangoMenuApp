from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models


def index(request):
    return render(request, 'menuApp/index.html', context={'menu': _get_menu()})


def select_menu(request, first_slug, second_slug=None, third_slug=None):
    menu = _get_menu()
    first_level_item = menu.filter(slug=first_slug).first()
    second_level_item = first_level_item.second_lvl.filter(slug=second_slug).first() if second_slug else None
    third_level_item = second_level_item.third_lvl.filter(slug=third_slug).first() if third_slug else None
    context = {
        'menu': menu,
        'first_level_item': first_level_item,
        'second_level_item': second_level_item,
        'third_level_item': third_level_item
    }
    return render(request, 'menuApp/selected_menu.html', context=context)


def _get_menu():
    return models.MenuItemFirstLvl.objects.all()