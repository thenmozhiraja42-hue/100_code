import math
from typing import List


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n (int): The number to check.

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
        count (int): Number of primes to generate.
        start_from (int): Starting integer to check for primality. Defaults to 101.

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


def main() -> None:
    """Read user input for prime count and print generated primes separated by commas."""
    n = int(input())
    primes = generate_primes(n)
    print(",".join(map(str, primes)))


if __name__ == "__main__":
    main()

