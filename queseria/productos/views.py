from django.shortcuts import render
from .models import Lista , Fiambre

def productos(request):
    listas = Lista.objects.all()
    fiambres = Fiambre.objects.all()
    return render(request, "productos/productos.html", 
                {
                    'listas':listas,
                    'fiambres':fiambres
                    } )

