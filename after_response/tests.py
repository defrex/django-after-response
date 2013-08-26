
from django.test import TestCase

from .decorators import enable


class AfterResponseTest(TestCase):

    def test_execution(self):
        self.executed = 0

        @enable
        def func(val):
            self.executed += 1

        self.assertEqual(self.executed, 0)
        self.client.get('/')
        self.assertEqual(self.executed, 0)

        func.after_response(True)

        self.assertEqual(self.executed, 0)
        self.client.get('/')
        self.assertEqual(self.executed, 1)

        func.after_response(True)
        func.after_response(True)

        self.assertEqual(self.executed, 1)
        self.client.get('/')
        self.assertEqual(self.executed, 3)
