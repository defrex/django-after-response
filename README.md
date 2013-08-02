[![Build Status](https://travis-ci.org/defrex/django-after-response.png)](https://travis-ci.org/defrex/django-after-response)

### Django After Response

Simple asynchronous execution.

Tools like [Celery](http://celeryproject.org/) are great, but often they are
overpowered for the task at hand, and come with lots of requirements like
daemons and task queues.

After Response is a simple alternative. It will execute code after the
request is complete, but do it in the current process and thread.

### Usage

    $ pip install django-after-request

Decorate your function.

    import after_response
    from django.core.mail import send_mail

    @after_response.enable
    def my_email_task(to, subject, body):
        send_mail(subject, body, 'me@example.com', [to])

Then, when you want to execute the function after the current request.

    my_email_task.after_response('customer@example.com', 'Confirm Signup', body)

That's it! Execution of your function will be deferred until after the
current request/response.
