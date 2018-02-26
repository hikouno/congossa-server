from django.db import models
from django.conf import settings
from django.template.defaultfilters import date as dj_date
from django.utils.translation import ugettext as _
from django.utils import timezone

from utilisateur.models import Utilisateur


class Dialog(models.Model):
    owner = models.ForeignKey(Utilisateur, related_name='owner', on_delete=models.CASCADE, blank=True)
    opponent = models.ForeignKey(Utilisateur, related_name='opponent', on_delete=models.CASCADE, blank=True)


class Message(models.Model):
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE, blank=True)
    sender = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, blank=True)
    text = models.TextField(max_length=200, blank=True)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
