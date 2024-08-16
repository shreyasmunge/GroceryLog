from django.contrib import admin
from .models import GroceryItem
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class GroceryItemAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','description')


admin.site.register(GroceryItem, GroceryItemAdmin)

