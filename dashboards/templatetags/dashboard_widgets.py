from django.template.defaulttags import register

from dashboards.models import User, Item


@register.inclusion_tag("dashboard.html")
def dashboard_widget():
    users = {"name": "Users", "count": User.objects.count()}
    items = {"name": "Items", "count": Item.objects.count()}
    return {"cards": [users, items]}


@register.inclusion_tag("dashboard_card.html")
def dashboard_card(values):
    return values
