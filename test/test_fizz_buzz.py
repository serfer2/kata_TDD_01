# coding: utf8

import unittest

from fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_it_raises_exception_when_value_is_not_a_number(self):
        with self.assertRaises(TypeError):
            fizz_buzz(value='a string')

    def test_it_returns_same_number_as_received(self):
        output = fizz_buzz(value=1)
        self.assertEqual(output, 1)


if __name__ == '__main__':
    unittest.main()
