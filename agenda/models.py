from django.db import models
from django.contrib.auth.models import User


class AgendaItem(models.Model):
    text = models.CharField(max_length=240)
