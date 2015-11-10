def removeDuplicates(nums):
    """
    Given a sorted array/list, remove duplicate numbers from array (in place) and return length.  On leetcode, while you only return the length, it also judged if you had right list so can't just have a counter.

    :type nums: List[int]
    :rtype: int
    """
    #index counters to compare items in array
    i = 0
    j = 1
    
    if len(nums) > 1:
        while j < len(nums):
            if nums[i] == nums[j]:
                del(nums[j])
            else:
                #because you are actually deleting an item in array, thus changing the indices only want to move index counters when you don't delete. 
                i += 1
                j += 1
    return len(nums)