"""

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""
nums1 = [1, 3]
nums2 = [2, 4]


list_final = nums1 + nums2
list_final.sort()
count = len(list_final)
if count % 2 == 0:
    result = (list_final[int(count/2)] + list_final[int(count/2) - 1])/ 2
else:
    result = (list_final[int(count/2)])

print(result)