import unittest
from random import randint
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from ro.core.exceptions import SignalException
from ro.core.signals import receiver, Signal


class BaseTestClass(unittest.TestCase):
    pass


class TestSignalsModule(BaseTestClass):

    @classmethod
    def setUpClass(cls):
        class Foo:
            pass

        cls.foo = Foo()
        cls.signal = Signal()

    def test_unregistered_signal_raises_signal_exception(self):
        with self.assertRaises(SignalException):
            self.signal.notify(self.foo)

        with self.assertRaises(SignalException):
            self.signal.remove_dispatch(self.foo, 'foo')


if __name__ == '__main__':
    unittest.main()
