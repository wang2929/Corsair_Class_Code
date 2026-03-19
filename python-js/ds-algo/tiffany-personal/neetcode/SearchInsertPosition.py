'''
You are given a sorted array of distinct integers and a target value
Return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        i, j = 0, len(nums)-1
        if target < nums[0]: return 0
        if target > nums[-1]: return len(nums)
        while i <= j:
            idx = i + (j - i + 1) // 2
            if nums[idx] == target:
                return idx
            elif nums[idx] < target and nums[idx+1] > target:
                return idx + 1
            elif nums[idx] > target:
                j = idx - 1
            else:
                i = idx + 1

nums = [1, 3, 5, 6]
target = 2
print(Solution().searchInsert(nums, target))
nums = [-1,0,2,4,6,8]
target = 5
print(Solution().searchInsert(nums, target))
nums=[1,4,6,8,10,12]
target=12
print(Solution().searchInsert(nums, target))
        