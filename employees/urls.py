from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'employees'

urlpatterns = [
    url(r'^$', views.index_view, name='home'),
    url(r'^about/', views.about_view, name='about'),
    url(r'^gallery/', views.gallery_view, name='gallery'),
    url(r'^contacts/', views.contact_view, name='contacts'),
    url(r'^employees/', views.employee_view, name='employees'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


