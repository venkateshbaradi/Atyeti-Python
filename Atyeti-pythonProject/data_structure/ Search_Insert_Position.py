"""

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""
class Solution(object):
    def searchInsert(self, nums, target):

        if target in nums:
            return nums.index(target)
        else:
            new_nums = nums[:]
            new_nums.append(target)
            new_nums.sort()
        return new_nums.index(target)
