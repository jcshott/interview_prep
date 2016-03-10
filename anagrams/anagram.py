"""Given a word list, find the word with the most anagrams in the list."""


def find_most_anagrams_from_wordlist(wordlist):
    """Given a list of words, return the word with the most anagrams.

    For a list of ['act', 'cat', 'bill']:
    - 'act' and 'cat' are anagrams, so they both have 2 matching words.
    - 'bill' has no anagrams, os it has one matching word (itself).

    Given that 'act' is the first instance of the most-anagrammed word,
    we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

    Let's use a file of words where each line is a word:

    >>> all_words = [w.strip() for w in open('words.txt')]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'
    """
    anagrams = {}

    for word in wordlist:
        sorted_word = ''.join(sorted(word))
        anagrams.setdefault(sorted_word, []).append(word)


    most_anagrams = []
    for val in anagrams.values():
        if len(val) > len(most_anagrams):
            most_anagrams = val

    return most_anagrams[0]


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
