
from django.contrib import admin
from django.urls import path, include
from AppGaleriaWeb.views import * 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('vicuDesign/', include('AppGaleriaWeb.urls')),
    #path('GaleriaVicuDesign/', include('AppGaleriaWeb.urls')),
    
    path('', include('AppGaleriaWeb.urls')),  # URL raíz para la aplicación
       
      
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)