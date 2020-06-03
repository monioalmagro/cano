from django.contrib import admin
from django.urls import path
from core import views as  core_views
from productos import views as productos_views
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name='home'),
    path('productos/', productos_views.productos, name='productos'),
    path('contact/', core_views.contact, name='contact'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


