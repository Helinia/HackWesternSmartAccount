
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Graph import urls
import GraphDescrip.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Graph/', include("Graph.urls")),
    path('accounts/', include('accounts.urls')),
    path('', GraphDescrip.views.home, name = 'home'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
