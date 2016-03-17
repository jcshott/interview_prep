"""Count from 1 to 20 in fizzbuzz fashion.

Loop from 1 to 20 (inclusive). Each through, if the number
is evenly divisible by 3, say 'fizz'. If the number is evenly
divisible by 5, say 'buzz'. If the number is evenly divisible
by both 3 and 5, say 'fizzbuzz'. Otherwise, say the number.

    >>> fizzbuzz()
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    17
    fizz
    19
    buzz
"""


def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion."""

    for x in range(1, 21):
        if x % 3 == 0 and x % 5 == 0:
            print "fizzbuzz"
        elif x % 3 == 0:
            print "fizz"
        elif x % 5 == 0:
            print "buzz"
        else:
            print x


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FIZZBUZZ FOR THE WIN!\n"