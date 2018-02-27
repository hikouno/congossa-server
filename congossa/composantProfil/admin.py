from django.contrib import admin

# Register your models here.
from .models import Competence
from .models import NiveauEtude
from .models import Qualite
from .models import Experience
from .models import Formation


admin.site.register(Competence)
admin.site.register(NiveauEtude)
admin.site.register(Qualite)
admin.site.register(Experience)
admin.site.register(Formation)

