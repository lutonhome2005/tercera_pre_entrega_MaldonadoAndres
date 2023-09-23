from django.contrib import admin
from django.urls import path, include
from AppGaleriaWeb.views import * 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('', index, name='index'),
    #path('galeria/', galerias),
    #path('artistas/',artistas),
    #path('registrarse/',registrarse),
    #path('formularioAltaArtista/', formularioAltaArtista, name='formularioAltaArtista'),
    
    
 
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)