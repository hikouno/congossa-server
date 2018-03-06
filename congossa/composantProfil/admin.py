from django.contrib import admin

# Register your models here.
from .models import Competence
from .models import Qualite
from .models import Experience
from .models import Formation
from .models import Metier



admin.site.register(Competence)
admin.site.register(Qualite)
admin.site.register(Experience)
admin.site.register(Formation)
admin.site.register(Metier)
