"""Personal context processor."""

from django.conf import settings


def from_settings(request):
    """Function."""
    return {
        'ENVIRONMENT_NAME': settings.ENVIRONMENT_NAME,
        'ENVIRONMENT_COLOR': settings.ENVIRONMENT_COLOR,
    }
