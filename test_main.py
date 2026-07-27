import unittest
from main import is_prime, generate_primes, get_fibonacci, collatz_steps


class TestAlgorithms(unittest.TestCase):

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

    def test_get_fibonacci(self):
        self.assertEqual(get_fibonacci(1), 0)
        self.assertEqual(get_fibonacci(2), 1)
        self.assertEqual(get_fibonacci(3), 1)
        self.assertEqual(get_fibonacci(6), 5)
        with self.assertRaises(ValueError):
            get_fibonacci(0)

    def test_collatz_steps(self):
        self.assertEqual(collatz_steps(1), 0)
        self.assertEqual(collatz_steps(2), 1)
        self.assertEqual(collatz_steps(12), 9)
        with self.assertRaises(ValueError):
            collatz_steps(0)


if __name__ == "__main__":
    unittest.main()
