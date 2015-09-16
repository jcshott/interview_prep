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
    word_dict = {}

    #create a dictionary where key is the word sorted. if a word sorted is already a key, its an anagram so add it to the value list, holding the anagrams found.

    for word in wordlist:
        s_word = "".join(sorted(word))
        word_dict.setdefault(s_word, [])
        word_dict[s_word].append(word)

    most_anagrams = []

    #go through the values of our dict (list of words that are anagrams of each other) and find longest - that which has the most anagrams
    for value in word_dict.values():
        if len(value) > len(most_anagrams):
            most_anagrams = value

    #once you have the most anagrams, you can return the first item in that value list, it'll be the first item you encountered (added to the value list)

    return most_anagrams[0]


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
