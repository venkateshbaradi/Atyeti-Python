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
if len(list_final) % 2 == 0:
    (list_final[len(list_final)/2] + list_final[len(list_final)/2 - 1]) / 2.0
else:
    float(list_final[len(list_final)/2])