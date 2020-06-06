from django.contrib import admin
from .models import Lista , Fiambre

class ListaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Lista,ListaAdmin)
admin.site.register(Fiambre)

