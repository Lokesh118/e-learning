"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
