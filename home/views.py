from Quilitienda.home.models import Categoria
from django.shortcuts import render

def home (request):
  total_categorias = Categoria.objects.all()
  context = {'total_categorias': total_categorias}
  return render(request, 'home/categorias.html', context)
