from django.contrib import admin
from django.urls import path, include
from clientes import urls as clients_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from home import urls as home_urls
urlpatterns = [
                  path('', include(home_urls)),
                  path('clients/', include(clients_urls)),
                  path('admin/', admin.site.urls),
                  path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
