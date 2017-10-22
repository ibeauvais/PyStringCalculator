class StringCalculator:
    def add(self, valueAsString):
        if not valueAsString:
            return 0

        numbers = map(int, valueAsString.split(","))
        return sum(numbers)
