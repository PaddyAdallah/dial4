from django.conf.urls import url, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

from .views import *

router = routers.DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    url(r'^employees/', include(router.urls)),
    url(r'^home/', index, name='home'),
    url(r'^about/', about, name='about'),
    url(r'^gallery/', gallery, name='gallery'),
    url(r'^contact/', contact, name='contact'),
    url(r'^/profile/', profile, name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
