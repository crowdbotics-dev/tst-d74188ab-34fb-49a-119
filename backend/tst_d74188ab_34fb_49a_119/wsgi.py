"""
WSGI config for tst_d74188ab_34fb_49a_119 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tst_d74188ab_34fb_49a_119.settings"
)

application = get_wsgi_application()
