from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import Utilisateur


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Utilisateur

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('description','sexe','telephone','dateDeNaissance','localisation','avatar','experience','qualite')}),
    )


# Register your models here.
admin.site.register(Utilisateur, MyUserAdmin)
