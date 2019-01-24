"""
WSGI config for Django2019 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from os.path import join,dirname,abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))

sys.path.insert(0,PROJECT_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Django2019.settings'
#path = '/home/ubuntu/workspace/Django2019'

#if path not in sys.path:
#    sys.path.insert(0, '/home/ubuntu/workspace/Django2019/Django2019')
#os.environ['DJANGO_SETTINGS_MODULE'] = 'Django2019.settings'

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django2019.settings")

application = get_wsgi_application()
