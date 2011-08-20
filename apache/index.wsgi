import os, sys

# activate virtualenv
activate_this = os.path.expanduser("~/sites/efo/pinax-env/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# tell django where our settings module is
sys.path.insert(0, os.path.expanduser("~/sites/efo"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'efo.settings'

# run django
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
