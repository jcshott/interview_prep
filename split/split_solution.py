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

    #check each letter of your word. if that letter is in the splitter, need to check if the rest of the word also matches splitter to determine if you really split or not.

    split_list = []
    temp_string = ""
    splitter_len = len(splitter)
    index_count = 0

    #need to keep track of where you are in the string, can't just iterate over each letter as that screws up the progression 
    #need to skip ahead in string when you hit a splitter
    while index_count < len(astring):
        #need to check whole splitter - could be a word.
        if astring[index_count:(index_count + splitter_len)] == splitter: 
            split_list.append(temp_string)
            temp_string = ""
            index_count = index_count + splitter_len #skip ahead in string by updating index counter
           
        else:
            temp_string = temp_string + astring[index_count]
            index_count = index_count + 1 #if you aren't skipping ahead b/c you hit splitter, one char is added at a time
    
    #have to make sure last word/phrase gets appeneded before returnin
    split_list.append(temp_string)

    return split_list

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FINE SPLITTING!\n"
