
import logging

from django.core.signals import request_finished

from .store import function_queue

logger = logging.getLogger(__name__)


def run_em_all(*args, **kwargs):
    for func, args, kwargs in function_queue:
        try:
            func(*args, **kwargs)
        except Exception as e:
            logger.exception(str(e))
request_finished.connect(run_em_all)
