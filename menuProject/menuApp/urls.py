from django.urls import path
from . import views


app_name = 'menu'
urlpatterns = [
    path('', views.index, name="show_menu"),
    path('<slug:first_slug>', views.select_menu, name="first_level"),
    path('<slug:first_slug>/<slug:second_slug>', views.select_menu, name="second_level"),
    path('<slug:first_slug>/<slug:second_slug>/<slug:third_slug>', views.select_menu, name="third_level")
]