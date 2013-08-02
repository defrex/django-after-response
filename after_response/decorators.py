
from .store import function_queue

def enable(func):
    def after_response(*args, **kwargs):
        function_queue.append((func, args, kwargs))
    func.after_response = after_response
    return func
