#!/usr/bin/python3
"""
Dynamic Programming Minimum operations
"""


def minOperations(n):
    """Function to return fewest no of operations to result in exactly
    n H characters in a file ."""
    if n == 1:
        return 0

    op = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            op += divisor
            n //= divisor
        else:
            divisor += 1
    return op
