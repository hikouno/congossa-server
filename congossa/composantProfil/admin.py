from django.contrib import admin

# Register your models here.
from .models import Competence
from .models import NiveauEtude
from .models import Qualite

admin.site.register(Competence)
admin.site.register(NiveauEtude)
admin.site.register(Qualite)