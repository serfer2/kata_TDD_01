# coding: utf8

import unittest

from fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_it_raises_exception_when_value_is_not_a_number(self):
        with self.assertRaises(TypeError):
            fizz_buzz(value='a string')

    def test_it_returns_same_number_as_received(self):
        # Acción
        output = fizz_buzz(value=1)
        # Comprobación
        self.assertEqual(output, 1)

    def test_it_returns_fizz_when_value_is_divisible_by_3(self):
        # Inicializo
        a_number_divisible_by_3 = 9
        expected_result = 'fizz'
        # Accion
        output = fizz_buzz(value=a_number_divisible_by_3)

        # Comprobación
        self.assertEqual(output, expected_result)

    def test_it_returns_buzz_when_value_is_divisible_by_5(self):
        a_number_divisible_by_5 = 10
        expected_result = 'buzz'

        output = fizz_buzz(value=a_number_divisible_by_5)

        self.assertEqual(output, expected_result)

    def test_it_returns_fizzbuzz_when_value_is_divisible_by_5_and_3(self):
        a_number_divisible_by_5_and_3 = 15
        expected_result = 'fizz buzz'

        output = fizz_buzz(value=a_number_divisible_by_5_and_3)

        self.assertEqual(output, expected_result)


if __name__ == '__main__':
    unittest.main()
