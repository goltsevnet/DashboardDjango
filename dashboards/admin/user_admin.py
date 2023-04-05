from django.contrib import admin
from dashboards.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "last_login",
        "groups_display",
        "is_active",
        "is_staff",
        "date_joined",
    )

    list_editable = (
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    )

    def groups_display(self, obj):
        return [group.name for group in obj.groups.all()]

    groups_display.short_description = "groups"
