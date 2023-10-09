from django.contrib import admin
from django.urls import path, include
from AppGaleriaWeb.views import * 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LogoutView



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('enviar_correo/', views.enviar_correo, name='enviar_correo'),
    path('enviar_consulta_artista/', views.enviar_consulta_artista, name='enviar_consulta_artista'),
    path('artistas/',artistas),
    path('galerias/', galerias),
    path('registrarse/',registrarse),
    path('email_exitoso/',email_exitoso,name='email_exitoso'),
    path('email_fallido/',email_fallido,name='email_fallido'),
    path('contactos/',contactos),
    path('nuestros_servicios/', views.nuestros_servicios, name='nuestros_servicios'),
    path('sobre_nosotros/', sobre_nosotros, name='sobre_nosotros'),
    path('pagina_en_construccion/', pagina_en_construccion, name='pagina_en_construccion'),
    path('formularioAltaArtista/', formularioAltaArtista, name='formularioAltaArtista'),
    path('registro/', registrar, name='registro'),
    path('registro_exitoso_obra_arte/', registro_exitoso_obra_arte, name='registro_exitoso_obra_arte'),
    path('aviso_registroArtista/', aviso_registroArtista, name='aviso_registroArtista'),
    path('formularioAltaUsuario/', formularioAltaUsuario, name='formularioAltaUsuario'),
    path('formularioAltaObraArte1/', formularioAltaObraArte1, name='formularioAltaObraArte1'),
    path('formularioAltaGaleria/', formularioAltaGaleria, name='formularioAltaGaleria'),# Nueva URL para dar de alta Galerias
    path('formularioAltaCarrito/', formularioAltaCarrito, name='formularioAltaCarrito'),#Nueva URL para dar de alta los Carritos
    path('lista_artistas/', lista_artistas, name='lista_artistas'),# Nueva URL para listar los artistas
    path('lista_galerias/', lista_galerias, name='lista_galerias'),# Nueva URL para listar los galerias
    path('buscar_artista/', buscar_artista, name='buscar_artista'),# Nueva URL para Buscar los artistas
    path('consulta_artista/<int:artista_id>/', consulta_artista, name='consulta_artista'),
    path('lista_obras_galeria/<int:galeria_id>/', views.lista_obras_galeria, name='lista_obras_galeria'),
    path('detalle_obra/<int:obra_id>/', views.detalle_obra, name='detalle_obra'),
    path('detalle_obra_galeria/<int:obra_id>/', views.detalle_obra_galeria, name='detalle_obra_galeria'),
    path('obras_por_artista/<int:artista_id>/', views.obras_por_artista, name='obras_por_artista'),
    path('consulta_artista/', views.consulta_artista, name='consulta_artista'),
    path('login_view/', login_view, name='login_view'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view (template_name="logout.html"), name='logout'),
]   



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

