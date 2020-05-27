from django.shortcuts import render
from .models import Lista

def productos(request):
    listas = Lista.objects.all()
    return render(request, "productos/productos.html", 
                {
                    'listas':listas
                    } )

