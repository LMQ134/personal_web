"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling  # 注意是 dj_static 不是 dj-static


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')

application = Cling(get_wsgi_application())
