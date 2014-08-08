[![Build Status](https://travis-ci.org/defrex/django-after-response.png)](https://travis-ci.org/defrex/django-after-response)
[![Pypi Package](https://badge.fury.io/py/django-after-response.png)](http://badge.fury.io/py/django-after-response)

### Django After Response

Simple asynchronous execution.

Tools like [Celery](http://celeryproject.org/) are great, but often they are
overpowered for the task at hand, and come with lots of requirements like
daemons and task queues.

After Response is a simple alternative. It will execute code after the
request is complete, without the need for additional daemons or task queues.

### Usage

    $ pip install django-after-response

Add `after_response` to your `INSTALLED_APPS`

    INSTALLED_APPS = (
        ...
        'after_response',
    )

Decorate your function.

    from django.core.mail import send_mail
    import after_response

    @after_response.enable
    def my_email_task(to, subject, body):
        send_mail(subject, body, 'me@example.com', [to])

Then, when you want to execute the function after the current request/response.

    my_email_task.after_response('customer@example.com', 'Confirm Signup', body)

That's it! Execution of your function will be deferred until after the
current request/response.

### Setting

Set `AFTER_RESPONSE_RUN_ASYNC` to `False` to prevent After Response from
executing the jobs in another thread.
