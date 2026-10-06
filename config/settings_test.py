from .settings import *  # noqa

CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}
SESSION_ENGINE = "django.contrib.sessions.backends.db"
CELERY_TASK_ALWAYS_EAGER = True
