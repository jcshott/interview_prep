"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""

def is_prime(num):
    
    if num < 2:
        return False

    # special case
    if num == 2:
        return True
    
    # even nums
    if num % 2 == 0:
        return False
    
    # check for whether odd num is prime
    n = 3

    while n * n <= num:
        if num % 3 == 0:
            return False
        n += 2

    return True


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    out = []
    eval_num = 0

    while len(out) != count:
        if is_prime(eval_num):
            out.append(eval_num)
        eval_num += 1

    return out


if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
