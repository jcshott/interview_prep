"""Is this word a palindrome?

    >>> is_palindrome("a")
    True

    >>> is_palindrome("noon")
    True

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("porcupine")
    False

Treat spaces and uppercase letters normally:

    >>> is_palindrome("Racecar")
    False
"""


def is_palindrome(word):
    """Return True/False if this word is a palindrome."""
    ## iterative solution. O(n) because we go through word once and check. at most we go through half the len(word)
    # if len(word) < 1:
    #     return False

    # if len(word) == 1:
    #     return True

    # for x in range(len(word)/2):
    #     if word[x] != word[-x-1]:
    #         return False

    # return True

    ## recursive solution 

    if len(word) < 2:
        return True
    return is_palindrome(word[1:-1]) and word[0] == word[-1]


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!"
