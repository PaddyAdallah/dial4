from django.conf.urls import url,include
from rest_framework import routers
from employees.views import PostViewSet
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    url(r'^employees/',include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)