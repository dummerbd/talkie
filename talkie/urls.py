from django.conf.urls import url, include
from django.contrib import admin

from .talkie import urls as talkie_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'', include(talkie_urls, namespace='talkie'))
]
