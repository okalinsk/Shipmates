from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('ship.urls')),
    url(r'^ship/', include('ship.urls')),
]
