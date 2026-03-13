from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while j < n:
            if nums1[i] != 0 and nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                nums1 = nums1[:i] + [nums2[j]] + nums1[i:-1]
                i += 1
                j += 1
            else:
                nums1[i] = nums2[j]
                i += 1
                j += 1

nums = [10,20,20,40,0,0]
Solution().merge(nums, 4, [1, 2], 2)
print(nums)

nums = [0, 0]
Solution().merge(nums, 0, [1, 2], 2)
print(nums)