from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, null=False)
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=False)
