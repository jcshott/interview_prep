def split(astring, splitter):
    """Split astring by splitter and return list of splits.

    This should work like that built-in Python .split() method [*].
    YOU MAY NOT USE the .split() method in your solution!
    YOU MAY NOT USE regular expressions in your solution!

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

    * Note: the actual Python split method has special behavior
      when it is not passed anything for the splitter -- you do
      not need to implemented that.
    """

    # find the index of the splitter, str.find(str2) method returns index of start of given str2 or -1 if not found
    # add everything before to the list, 
    # increment start of the find index to end of splitter

    start_idx = 0
    split_array = []

    # while we haven't hit end of string
    while start_idx <= len(astring):
        found_idx = astring.find(splitter, start_idx)
        # if we don't find the splitter, add everything to the array
        if found_idx == -1:
            split_array.append(astring[start_idx:])
            break
        else:
            # append everything up to the splitter to array
            split_array.append(astring[start_idx:found_idx])
            # move the start index to after the splitter
            start_idx = found_idx + len(splitter)
    return split_array



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FINE SPLITTING!\n"
