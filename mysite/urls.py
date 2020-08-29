from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url


urlpatterns = [
    # url pour l'administration
    path('admin/', admin.site.urls),
    # url pour forwarder immEdiatement vers lycee au demarrage (avec url vide)
    url(r'^', include('lycee.urls')), 
    url(r'^lycee/', include('lycee.urls')),
    #path(r'^lycee/' ,  lycee.urls),
    #url(r'^lycee/', include('lycee.urls', "lycee","lycee")),
    
]