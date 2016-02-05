"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8
    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 8, 9], 10)
    10
    """
    # # O(n) runtime because have to go through whole list. twice, really.

    # num_dict = {}

    # # create a dictionary of nums we have for O(1) look-up.
    # for x in nums:
    # 	num_dict[x] = True

    # # go through all possible nums and return the one we don't have in our dict.
    # for item in range(1, max_num+1):
    # 	if item not in num_dict:
    # 		return item

    # initialize a new list to fill in
    new_lst = [None] * max_num

    # add each num we have to the new_lst at index it should be at (i.e. 1 at idx=0, etc)
    for x in nums:
        new_lst[x-1] = x

    return new_lst.index(None) + 1


    # O(n log n) sort and then go through once to check

    # sorted_nums = sorted(nums)

    # if sorted_nums[-1] != max_num:
    #     return max_num

    # for idx, num in enumerate(sorted_nums):
    #     if num != idx+1:
    #         return idx+1


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"
