"""
WSGI config for tw_perm_data_analysis_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tw_perm_data_analysis_web.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
