#from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
#from django.core.wsgi import get_wsgi_application
import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
#site.addsitedir('~/.virtualenvs/myprojectenv/local/lib/python2.7/site-packages')
#site.addsitedir(os.path.join( os.path.dirname(__file__), 'public', 'static'))

path = os.path.dirname(__file__) # '/var/www/html/przedszkole32'  # use your own username here
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'przedszkole32.settings'

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(get_wsgi_application())
#from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
#application = Sentry(get_wsgi_application())
#application = get_wsgi_application()
