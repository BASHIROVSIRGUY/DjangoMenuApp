from django.contrib import admin
from . import models

admin.site.register(models.MenuItemFirstLvl, admin.ModelAdmin)
admin.site.register(models.MenuItemSecondLvl, admin.ModelAdmin)
admin.site.register(models.MenuItemThirdLvl, admin.ModelAdmin)