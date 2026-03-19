'''
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.',
return the number of that contain:
    - grid[0][0]
    - an equal frequency of 'X' and 'Y'.
    - at least one 'X'.
'''
class Solution:
    def CalculateState(self, grid, rows, cols):
        val, contains_X = 0, False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'X':
                    val += 1
                    contains_X = True
                elif grid[i][j] == 'Y':
                    val -= 1
        if contains_X and val == 0:
            return 1
        return 0

    def numberOfSubmatrices(self, grid) -> int:
        ret = 0
        rows, cols = len(grid), len(grid[0])
        prefix_sum = []
        # contains X is a problem
        for i in range(rows):
            val = 0
            # prefix sum by rows
            for j in range(cols):
                if grid[i][j] == 'X':
                    val += 1
                    prefix_sum[i].append(val)
                elif grid[i][j] == 'Y':
                    val -= 1
                    prefix_sum[i].append(val)
                else:
                    prefix_sum[i].append(val)
                if prefix_sum[0][cols] + prefix_sum[i][cols] == 0:
                    ret += 1
        return ret

print(Solution().numberOfSubmatrices([["X","Y","."],["Y",".","."]]))
print(Solution().numberOfSubmatrices([["X","X"],["X","Y"]]))
print(Solution().numberOfSubmatrices([[".","."],[".","."]]))
print(Solution().numberOfSubmatrices([[".","."],["Y","X"]]))