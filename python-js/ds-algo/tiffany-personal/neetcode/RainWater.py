'''
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
Return the maximum area of water that can be trapped between the bars.
'''

class Solution:
    def trap(self, height) -> int:
        # algo doesn't work and two sticks next to each other can't hold water
        if len(height) <= 2:
            return 0
        
        ret = 0
        i = 0
        # check left -> right for boxes where the right side is equal or longer
        while i < len(height):
            if height[i] == 0:
                i += 1
                continue
            subtract_area = 0
            for j in range(i+1, len(height)):
                if height[j] >= height[i]:
                    # can trap water here
                    ret += (height[i])*(j-i-1) - subtract_area
                    j -= 1  # correction for the for-loop
                    break
                else:
                    subtract_area += height[j]
            i = j + 1  # to exit for-loop or continue
            j += 1
        
        # check right -> left where left strictly greater
        i = len(height) - 1
        while i >= 0:
            if height[i] == 0:
                i -= 1
                continue
            subtract_area = 0
            for j in range(i-1, -1, -1):
                if height[j] > height[i]:
                    # can trap water here
                    ret += (height[i])*(i-j-1) - subtract_area
                    j += 1  # correction for the for-loop
                    break
                else:
                    subtract_area += height[j]
            i = j - 1  # to exit for-loop or continue
            j -= 1
        return ret
# could refactor maybe to remove some duplicate code (left to right vs right to left loop)
print(Solution().trap([4,2,0,3,2,5])) # 9
print(Solution().trap([4,2,3])) # 1
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(Solution().trap([0,2,0,3,1,0,1,3,2,1])) # 9