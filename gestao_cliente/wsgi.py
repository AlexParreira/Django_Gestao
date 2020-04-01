
import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_cliente.settings')

application = Cling(get_wsgi_application())
