from django.views.generic import View
from django.shortcuts import render


# Existen dos tipos de vista: Clases y de Funciones
# Esto es una vista de Clases
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'index.html', context)