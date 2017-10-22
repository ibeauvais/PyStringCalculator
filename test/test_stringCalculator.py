from unittest import TestCase

from StringCalculator import StringCalculator


class TestStringCalculator(TestCase):
    def test_add_with_empty(self):
        """should return 0 for empty string"""
        # Given
        input = ""
        stringcalculator = StringCalculator()

        # When
        result = stringcalculator.add(input)

        # Then
        self.assertEqual(result, 0)

    def test_add_with_one_number(self):
        """should return the number with only one number"""
        # Given
        input = "3"
        stringcalculator = StringCalculator()

        # When
        result = stringcalculator.add(input)

        # Then
        self.assertEqual(result, 3)

    def test_add_with_two_number(self):
        """should return sum of numbers with two numbers"""
        # Given
        input = "3,4"
        stringcalculator = StringCalculator()

        # When
        result = stringcalculator.add(input)

        # Then
        self.assertEqual(result, 7)

    def test_add_with_space_as_separator(self):
        """should return_sum when space is separator("""
        # Given
        input = "3 4"
        stringcalculator = StringCalculator()

        # When
        result = stringcalculator.add(input)

        # Then
        self.assertEqual(result, 7)
