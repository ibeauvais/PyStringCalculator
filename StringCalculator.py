import re


class StringCalculator:
    def __init__(self):
        self.splitRegex = re.compile("[,|\s]")

    def add(self, valueAsString):
        if not valueAsString:
            return 0

        numbers = map(int, self.splitRegex.split(valueAsString))
        return sum(numbers)
