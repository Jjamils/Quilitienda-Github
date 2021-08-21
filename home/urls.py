from django.urls import path
from .import views

#Importacionses para trabajar imagenes
#from django.conf import settings
#from django.conf.urls.static import static

app_name = 'home'
urlpatterns = [
  path('', views.home, name = 'home')
  
]


#URL para las imagenes
#if settings.DEBUG:
  #urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
