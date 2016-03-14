"""Reverse a string.

For example::

    >>> rev_string("")
    ''

    >>> rev_string("a")
    'a'

    >>> rev_string("porcupine")
    'enipucrop'

"""


def rev_string(astring):
    """Return reverse of string.

    You may NOT use the reversed() function!
    """
    #### List answer - 2 O(N) aka O(N) because 2 loops but not nested. 2 O(N) space
    # ltr_lst = list(astring)

    # out = ""

    # for x in range(len(ltr_lst)):
    #     out = out + ltr_lst.pop()
    
    # return out

    ### Recursion answer 
    # if len(astring) <= 1:
    #     return astring
    # return rev_string(astring[1:]) + astring[0]

    ### Reverse list method O(N) time and space because 1 while loop and the new list

    # ltr_lst = list(astring)

    # a = 0
    # z = -1

    # while a < len(ltr_lst)/2:
    #     ltr_lst[a], ltr_lst[z] = ltr_lst[z], ltr_lst[a]
    #     a = a+ 1
    #     z = z-1

    # return "".join(ltr_lst)

    out = ""

    # go through the length of the string, backwards
    for i in range(len(astring), 0, -1):
        # grab the char at the index minus 1. if we have range(len(astring) - 1, 0, -1), 
        #we miss the last char because it doesn't incl the astring[0] char.
        # if we do it this way, then we don't have an index error and we grab last char because 1-1 = 0 and we never hit 0-1
        out += astring[i-1]
    return out


if __name__ == '__main__':

    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !KROW DOOG\n"
