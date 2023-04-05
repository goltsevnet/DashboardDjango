from django.contrib import admin
from dashboards.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
