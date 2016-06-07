import os, sys
sys.path.append('/var/www/html/jaPedi/')
os.environ['DJANGO_SETTINGS_MODULE']='jaPedi.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

