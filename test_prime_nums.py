import unittest

from prime_nums import generate_prime_nums

class TestPrimeNumbers(unittest.TestCase):
    def setUp(self):
        self.prime_numbers = generate_prime_nums(10)
        
    def test_prime_nums_is_a_list(self):
        self.assertTrue(type(self.prime_numbers) is list, 
        "generate_prime_numbers should return a list.")
        
    def test_prime_nums_produces_correct_output(self):
        self.assertEqual(self.prime_numbers, [2, 3, 5, 7], 
        "Should produce correct output")
        
    def test_prime_nums_raises_TypeError_on_string_input(self):
        with self.assertRaises(TypeError):
            generate_prime_nums('10')
            
    def test_prime_nums_raises_ValueError_on_negative_input(self):
        with self.assertRaises(ValueError):
            generate_prime_nums(-1)
            
    def test_prime_nums_returns_correct_output_for_large_numbers(self):
        self.prime_numbers = generate_prime_nums(20)
        self.assertTrue(self.prime_numbers, [2, 3, 5, 7, 11, 13, 17, 19])
        
    def test_prime_nums_returns_empty_list(self):
        self.prime_numbers = generate_prime_nums(0)
        self.assertEqual(self.prime_numbers, [], 
        "Should return an empty list for input of 0")

if __name__ == '__main__':
    unittest.main()