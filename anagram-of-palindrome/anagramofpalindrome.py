"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    # a palindrome has the an even number of each letter - except possibly 1 letter (a middle letter)
    # so our word must follow that rule. 
    # we could iterate throug the word and add characters as key in dict value would be number of times present
    # we would check all the values, and if there is more than 1 odd value, we know it break palid rule

    letter_count = {}

    for char in word:
        letter_count[char] = letter_count.get(char, 0) + 1

    num_odd = 0

    for x in letter_count.values():
        if x % 2 != 0:
            num_odd += 1
        if num_odd == 2:
            return False
    return True



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
