def merge_meetings(times):
    """
    Function to condense meeting times.

    Input: a list of meeting time ranges as tuples of integers (start_time, end_time). not necessarily in order
    These integers represent the number of 30-minute blocks past 9:00am.

    Return: a list of condensed ranges.
    For example, given:

    >>> merge_meetings([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    >>> merge_meetings([(1, 5), (2, 3)])
    [(1, 5)]

    >>> merge_meetings([(1, 2), (2, 3)])
    [(1, 3)]

    >>> merge_meetings([(1, 10), (2, 6), (3, 5), (7, 9)])
    [(1, 10)]

    >>> merge_meetings([(1,4)])
    [(1, 4)]

    """
    # sort the times by first num in tuple
    sorted_times = sorted(times)
    out = []
    # tuple of (beginning, end)
    last_mtg = sorted_times[0]
    # sorted_times is array of tuples: [(1,2), (2,4), (4,6)]
    # need to know if we merge the times
    for curr_beginning, curr_end in sorted_times[1:]:
        # if meeting time we are looking at starts before or at same time as current meeting, merge them
        if curr_beginning <= last_mtg[1]:
            last_mtg = (last_mtg[0], max(curr_end, last_mtg[1]))
        # otherwise, add the last merged meeting (last_mtg) to the out array and reset last_mtg to current
        else:
            out.append(last_mtg)
            last_mtg = (curr_beginning, curr_end)

    out.append(last_mtg)
    return out

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "all tests pass"
