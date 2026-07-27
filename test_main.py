import unittest
from main import is_prime, generate_primes


class TestPrimeGenerator(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(103))
        self.assertFalse(is_prime(105))

    def test_generate_primes_count(self):
        primes = generate_primes(5, start_from=101)
        expected = [101, 103, 107, 109, 113]
        self.assertEqual(primes, expected)
        self.assertEqual(len(primes), 5)


if __name__ == "__main__":
    unittest.main()
