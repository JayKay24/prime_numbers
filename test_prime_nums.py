import unittest
from prime_nums import generate

class TestPrimeNumbers(unittest.TestCase):
    def setUp(self):
        self.prime_numbers = generate_prime_nums(10)
    def test_prime_nums_is_a_list(self):
        self.assertTrue(type(self.prime_numbers) is list, 
        "generate_prime_numbers should return a list.")

if __name__ == '__main__':
    unittest.main()