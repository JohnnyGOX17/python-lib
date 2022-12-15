#!/usr/bin/env python3
#
# Performs basic example of recursion to show the factorial of a given number n
#


def factorial(n):
    """
    Returns the factorial n! for a given positive integer n.

    n! = 1 if n=0, n*(n-1)! when n>=1
    """
    if n < 0:
        print("n must be a positive integer")
        raise ValueError
    elif n == 0:
        return 1
    else:
        # recursively implement factorial
        return n * factorial(n - 1)


if __name__ == "__main__":
    for i in range(6):
        print(f"Factorial of {i} is ", factorial(i))

    try:
        factorial(-4)
    except ValueError:
        print("Expected value error hit for negative factorial")
