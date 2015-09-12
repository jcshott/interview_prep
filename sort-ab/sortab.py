def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().

    Check edge cases of empty lists:

        >>> sort_ab([], [])
        []

        >>> sort_ab([1, 2,3], [])
        [1, 2, 3]

        >>> sort_ab([], [1, 2, 3])
        [1, 2, 3]

    Check:

        >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
        [1, 2, 3, 5, 6, 7, 8, 10]
    """
    output = []
    i = 0
    j = 0

    #need quit the loop once you have gone through a whole list so don't error out of range.
    #append the lower item and move the index for the list that it was in up.
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            output.append(a[i])
            i += 1
        else:
            output.append(b[j])
            j += 1
    
    #check if either of the lists haven't been all the way checked, if so, add on what is left
    if i < len(a):
        output.extend(a[i:])
        return output

    elif j < len(b):
        output.extend(b[j:])
        return output

    else:
        return output

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n"
