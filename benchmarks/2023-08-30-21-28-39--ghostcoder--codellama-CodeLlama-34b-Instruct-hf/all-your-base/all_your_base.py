import unittest
def rebase(input_base, digits, output_base):
    """
    Convert a number, represented as a sequence of digits in one base, to any other base.
    
    Parameters:
        input_base (int): The base of the input number
        digits (list): The digits of the input number, represented as a list of integers
        output_base (int): The base to convert the number to
    
    Returns:
        A list of integers representing the digits of the input number in the output base
    """
    # Calculate the value of the input number in base 10
    input_value = 0
    for digit in digits:
        input_value = input_value * pow(input_base, digit)

    # Convert the input value to the output base
    output_digits = []
    while input_value > 0:
        output_digits.append(input_value % output_base)
        input_value //= output_base

    return output_digits[::-1]

class TestRebase(unittest.TestCase):
    def test_rebase(self):
        self.assertEqual(rebase(2, [1, 0, 1], 10), [5, 2])
        self.assertEqual(rebase(2, [1, 0, 1], 2), [1, 0, 1])
        self.assertEqual(rebase(10, [1, 2, 3], 2), [1, 1, 0, 1])
        self.assertEqual(rebase(10, [1, 2, 3], 8), [1, 4, 3])
        self.assertEqual(rebase(16, [1, 2, 3, 4, 5], 2), [1, 0, 0, 1, 0, 1, 1, 0])

if __name__ == '__main__':
    unittest.main()
