
from __future__ import unicode_literals, print_function
import logging
import threading

from django.core.signals import request_finished

from .store import function_queue

logger = logging.getLogger(__name__)


def run(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except Exception as e:
        logger.exception(str(e))


def run_em_all(sender, **kwargs):
    while len(function_queue):
        func, args, kwargs = function_queue.pop()
        threading.Thread(target=run, args=(func,) + args, kwargs=kwargs).start()
request_finished.connect(run_em_all)
