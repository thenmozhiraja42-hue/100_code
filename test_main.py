import io
import sys
import unittest
from main import (
    is_prime,
    generate_primes,
    get_fibonacci,
    collatz_steps,
    print_multiplication_table,
    number_guessing_game,
)


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

    def test_print_multiplication_table(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_multiplication_table(5)
        finally:
            sys.stdout = sys.__stdout__
        lines = captured_output.getvalue().strip().split("\n")
        self.assertEqual(len(lines), 10)
        self.assertEqual(lines[0], "5 x 1 = 5")
        self.assertEqual(lines[-1], "5 x 10 = 50")

    def test_number_guessing_game(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sys.stdin = io.StringIO("3\n7\n10\n")
        try:
            number_guessing_game(target=10)
        finally:
            sys.stdout = sys.__stdout__
            sys.stdin = sys.__stdin__
        output = captured_output.getvalue().strip().split("\n")
        self.assertEqual(output, ["wrong try again", "wrong try again", "correct"])


if __name__ == "__main__":
    unittest.main()
