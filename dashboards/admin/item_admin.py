from django.contrib import admin
from dashboards.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("_name", "user")

    def _name(self, obj):
        return f"{obj.name[:25]}..."
