from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
from django.conf import settings
from django.template.defaultfilters import date as dj_date
from django.utils.translation import ugettext as _

from utilisateur.models import Utilisateur


class Dialog(models.Model): 
    owner = models.ForeignKey(Utilisateur, verbose_name=_("Dialog owner"), related_name="selfDialogs")
    opponent = models.ForeignKey(Utilisateur, verbose_name=_("Dialog opponent"))

class Message(TimeStampedModel, SoftDeletableModel):
    dialog = models.ForeignKey(Dialog, verbose_name=_("Dialog"), related_name="messages")
    sender = models.ForeignKey(Utilisateur, verbose_name=_("Author"), related_name="messages")
    text = models.TextField(verbose_name=_("Message text"))
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

