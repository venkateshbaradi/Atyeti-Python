class Solution(object):
    def removeDuplicates(self, nums):

        i = 1

        for j in range(1 , len(nums)):
        # j = 2 , i =1 ------> j = 3 , i = 2 --------->  j = 4 , i = 2  --------> j = 5 , i = 3 --------> j = 7 , i = 3

            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        return i


nums = [1, 1, 2, 2, 3, 3, 3, 4]
sol = Solution()
k = sol.removeDuplicates(nums)
