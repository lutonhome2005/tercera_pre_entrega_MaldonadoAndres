
from django.contrib import admin
from django.urls import path, include
from AppGaleriaWeb.views import * 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vicuDesign/', include('AppGaleriaWeb.urls')),
    
    
    
    
    #path('', index, name='index'),
    path('index/', index, name='index'),
    path('artistas/',artistas),
    path('galerias/', galerias),
    path('registrarse/',registrarse),
    path('contactos/',contactos),
    path('formularioAltaArtista/', formularioAltaArtista, name='formularioAltaArtista'),
    path('registro/', registrar, name='registro'),
    path('formularioAltaUsuario/', formularioAltaUsuario, name='formularioAltaUsuario'),
    path('formularioAltaObraArte/', formularioAltaObraArte, name='formularioAltaObraArte'),# Nueva URL para dar de alta obras de arte
    path('formularioAltaGaleria/', formularioAltaGaleria, name='formularioAltaGaleria'),# Nueva URL para dar de alta Galerias
    path('formularioAltaCarrito/', formularioAltaCarrito, name='formularioAltaCarrito'),#Nueva URL para dar de alta los Carritos
    path('lista_artistas/', lista_artistas, name='lista_artistas'),# Nueva URL para listar los artistas
    path('lista_galerias/', lista_galerias, name='lista_galerias'),# Nueva URL para listar los galerias
    
    
    
    path('buscar_artista/', buscar_artista, name='buscar_artista'),# Nueva URL para Buscar los artistas
    path('lista_obras_galeria/<int:galeria_id>/', views.lista_obras_galeria, name='lista_obras_galeria'),
    path('detalle_obra/<int:obra_id>/', views.detalle_obra, name='detalle_obra'),
    
    
]   

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)