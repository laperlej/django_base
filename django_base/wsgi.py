import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/home/galaxy/django_base/django_base')
sys.path.append("/home/galaxy/django_base/Library/Python2.7/bin")
sys.path.append("/home/galaxy/django_base/.local/bin")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_base.settings.base")

from dj_static import Cling
application = Cling(get_wsgi_application())
