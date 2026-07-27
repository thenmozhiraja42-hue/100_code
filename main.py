import math
from typing import List


# ------------------------------------------------------------------------------
# 1. Prime Number Generator (Starting from 101)
# ------------------------------------------------------------------------------
def is_prime(n: int) -> bool:
    """Check if a number is prime using 6k +/- 1 optimization.

    Args:
        n (int): The integer to test for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = math.isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def generate_primes(count: int, start_from: int = 101) -> List[int]:
    """Generate the first `count` prime numbers starting from `start_from`.

    Args:
        count (int): Number of prime numbers to generate.
        start_from (int): Starting number for the search. Defaults to 101.

    Returns:
        List[int]: List of generated prime numbers.
    """
    primes: List[int] = []
    num = start_from
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def print_primes_from_101(n: int) -> None:
    """Print the first `n` prime numbers starting from 101 as a comma-separated string."""
    primes = generate_primes(n, start_from=101)
    print(",".join(map(str, primes)))


# ------------------------------------------------------------------------------
# 2. Fibonacci Number Calculation (1-indexed)
# ------------------------------------------------------------------------------
def get_fibonacci(n: int) -> int:
    """Calculate the n-th Fibonacci number (1-indexed: 1st=0, 2nd=1, 3rd=1, 4th=2, ...).

    Args:
        n (int): 1-based index of the Fibonacci sequence.

    Returns:
        int: The n-th Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if n == 1:
        return 0
    if n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


# ------------------------------------------------------------------------------
# 3. Collatz Conjecture Step Counter
# ------------------------------------------------------------------------------
def collatz_steps(n: int) -> int:
    """Count the total steps to reach 1 in the Collatz sequence for starting value `n`.

    Args:
        n (int): Starting positive integer.

    Returns:
        int: Total number of steps.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def main() -> None:
    """Run all three algorithms sequentially based on user input."""
    try:
        n = int(input())
        print_primes_from_101(n)
        
        n_fib = int(input())
        print(get_fibonacci(n_fib))

        n_collatz = int(input())
        print(collatz_steps(n_collatz))
    except (ValueError, EOFError):
        pass


if __name__ == "__main__":
    main()


