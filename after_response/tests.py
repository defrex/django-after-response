
from django.test import TestCase

from .decorators import enable


class AfterResponseTest(TestCase):

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
