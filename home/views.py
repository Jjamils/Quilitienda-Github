from django.shortcuts import render
from .models import Producto

#Funcion para listar los productos y condicion para realizar la busqueda por productos
def home (request):
  total_productos = Producto.objects.all()
  context = {'total_productos': total_productos}

  item_name =request.GET.get('item_name')
  if item_name != '' and item_name is not None:
    total_productos = total_productos.filter(nombre = item_name)
  return render(request, 'home/home.html', context)
