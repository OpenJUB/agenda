from django.db import models


class AgendaItem(models.Model):
    text = models.CharField(max_length=240)
