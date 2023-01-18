from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Clothes, UserClotheRelation


@admin.register(Clothes)
class ClothesAdmin(ModelAdmin):
    pass


@admin.register(UserClotheRelation)
class UserRelationAdmin(ModelAdmin):
    pass
