class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        #initialize the array of sums since the nums array doesn't change
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #find the sum at j+1 (b/c starts at 0) and subtract the sum you got at i becasue that will filter out everything that came before nums[i]
        return self.sums[j + 1] - self.sums[i]

# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1,2,5,7])
print numArray.sums
print numArray.sumRange(0, 1)
print numArray.sumRange(1, 2)