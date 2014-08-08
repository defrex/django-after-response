
import time
from django.test import TestCase
from .decorators import enable


class AfterResponseTest(TestCase):

    def test_execution(self):
        self.executed = 0

        @enable
        def func(val):
            if val:
                self.executed += 1

        self.assertEqual(self.executed, 0)
        self.client.get('/')
        time.sleep(0.1)
        self.assertEqual(self.executed, 0)

        func.after_response(True)

        self.assertEqual(self.executed, 0)
        self.client.get('/')
        time.sleep(0.1)
        self.assertEqual(self.executed, 1)

        func.after_response(True)
        func.after_response(True)

        self.assertEqual(self.executed, 1)
        self.client.get('/')
        time.sleep(0.1)
        self.assertEqual(self.executed, 3)

        func.after_response(False)
        func.after_response(True)

        self.assertEqual(self.executed, 3)
        self.client.get('/')
        time.sleep(0.1)
        self.assertEqual(self.executed, 4)

    def test_slow_execution(self):
        self.executed = 0

        @enable
        def slow_func():
            time.sleep(1)
            self.executed += 1

        slow_func.after_response()

        self.assertEqual(self.executed, 0)
        self.client.get('/')
        self.assertEqual(self.executed, 0)

        slow_func.after_response()

        before_time = time.time()
        self.client.get('/')
        after_time = time.time()
        self.assertTrue(after_time - before_time < 0.5)
