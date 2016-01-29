import random


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).

    Given the numbers 1-10, return `n` random numbers, making sure
    to never return the same number twice. You can trust that this
    function will never be called with n < 0 or n > 10.

    It's tricky to test random functions! However, we can make sure
    asking for zero numbers gives us an empty list:

        >>> lucky_numbers(0)
        []

    And if we ask for all numbers, we shouldn't get any repeats:

        >>> sorted(lucky_numbers(10))
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    lucky_set = set()

    while len(lucky_set) < n:
        x = random.choice(range(1, 11))
        lucky_set.add(x)

    lucky_lst = list(lucky_set)
    return lucky_lst
    # lucky_nums = []

    # if n > 0:
    #     while len(lucky_nums) != n:
    #         x = random.choice(range(1, 11))
            
    #         if x not in lucky_nums:
    #             lucky_nums.append(x)

    #     return lucky_nums
    
    # else:
    #     return lucky_nums


if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
