from django.contrib import admin
from .models import Lista

class ListaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Lista,ListaAdmin)

