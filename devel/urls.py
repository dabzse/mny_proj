from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='home'),
    path('devel/', views.devel, name='devel'),
    path('cv/', views.cv, name='cv'),
    path('cert/', views.cert, name='cert_all'),
    path('cert/<str:filter_by>/', views.cert, name='cert_filter'),
    path('affiliates/', views.affiliates, name='affiliates'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
