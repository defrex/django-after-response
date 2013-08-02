
from django.conf.urls import patterns, url
from django.views.generic import View
from django.test import TestCase

from .decorators import enable


class AfterResponseTest(TestCase):
    urls = patterns('', url('', View.as_view()))

    def test_execution(self):
        self.executed = False

        @enable
        def func(val):
            self.executed = val

        self.assertFalse(self.executed)
        self.client.get('/')
        self.assertFalse(self.executed)

        func.after_response(True)

        self.assertFalse(self.executed)
        self.client.get('/')
        self.assertTrue(self.executed)
