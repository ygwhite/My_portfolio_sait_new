from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Clothes


@admin.register(Clothes)
class ClothesAdmin(ModelAdmin):
    pass
