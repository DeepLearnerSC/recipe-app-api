from django.test import TestCase

from app.cal import add, subtract
# Django searches for any Python module starting with "test". This is why you can store your tests in "tests.py" or "tests/test_something.py"

class CalcTests(TestCase):
    def test_add_numbers(self):
        """ Test that two numbers are added together"""
        self.assertEqual(add(8, 4), 12)

    def test_subtract_numbers(self):
        """ Test that two numbers are added together"""
        self.assertEqual(subtract(8, 12), 4)
