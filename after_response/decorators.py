
from django.conf import settings
from .store import function_queue


AFTER_RESPONSE_IMMEDIATE = getattr(settings, 'AFTER_RESPONSE_IMMEDIATE', False)


def enable(func):
    def after_response(*args, **kwargs):
        if AFTER_RESPONSE_IMMEDIATE:
            func(*args, **kwargs)
        else:
            function_queue.append((func, args, kwargs))
    func.after_response = after_response
    return func
