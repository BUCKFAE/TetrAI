import unittest

from src import adder
class Test_TestAdder(unittest.TestCase):

    def test_increment(self):
        print("Testing")
        self.assertEqual(2, adder.increment(1))