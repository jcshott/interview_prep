"""Using a binary search, find val in a range of 1-100. Return # of guesses.

Construct a list of 1-100 (inclusive). Write a binary search that searches
for val in that list (val will always be a number between 1 and 100).

Return the number of searches it took to find val. For a proper binary search
of 1-100, this should never be more than 7.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
"""

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    guess = None
    
    high_bound = 101
    low_bound = 0

    while guess != val:
        num_guesses += 1

        # need to add the lower bound otherwise our guess will always be too low
        # i.e. if we guess 50 but val = 25
        # we move bounds to 50 -> 101 but (101-50)/2 == 25 
        # so we'll never get to higher than 50 nums unless we add the 50 back in to get 75
        guess = (high_bound - low_bound)/2 + low_bound

        if guess < val:
            low_bound = guess
        elif guess > val:
            high_bound = guess

    return num_guesses


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n"


