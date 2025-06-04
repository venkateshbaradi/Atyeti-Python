class Solution(object):
    def removeElement(self, nums):

        count = len(nums)
        num = 0
        result = []

        for i in range(count):
            power = 10 ** (count - (i + 1))
            num += nums[i] * power

        final_num = (num + 1)
        print(final_num)
        while final_num > 0:
            digit = final_num % 10  # Get last digit (e.g., 4)
            result.insert(0, digit)  # Insert at the beginning
            final_num = final_num // 10

        return result


nums = [9, 3, 2]
sol = Solution()
print(sol.removeElement(nums))

