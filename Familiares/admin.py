from django.contrib import admin

from Familiares.models import Familia

class FamiliAdmin(admin.ModelAdmin):

    list_display= ('nombre', 'apellido', 'annonacimiento', 'parentezco')

admin.site.register(Familia,FamiliAdmin)


