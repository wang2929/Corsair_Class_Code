'''
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
A grid is said to be valid if all the cells above the main diagonal are zeros.
Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.
The main diagonal of a grid is the diagonal that starts at cell (0, 0) and ends at cell (n-1, n-1).
'''

class Solution:
    def minSwaps(self, grid) -> int:
        # need to check both left and right
        row_zero_count = []
        zero_to_row = {}
        for row in range(len(grid)):
            for i in range(1, len(grid) + 1):
                if grid[row][-i:] != [0] * i:
                    break
            row_zero_count.append(i-1)
            if (i-1) in zero_to_row:
                zero_to_row[i-1].append(row)
            else:
                zero_to_row[i-1] = [row]
        if sum(row_zero_count) < ((len(grid) ** 2 - len(grid)) // 2):
            return -1 # cannot solve
        i = len(grid) - 1
        solved = True
        for z in row_zero_count:
            if z < i:
                solved = False
                break
            i -= 1
        if solved:
            return 0 # already correct
        ending_position = 0
        row_order = list(range(len(grid)))
        swaps = 0
        for size in range(len(grid)-1, 0, -1):
            # I added rows to the dictionary from closest to farthest from the
            # ending position, so I'll just take the first one
            try:
                for idx in row_order:
                    if idx in zero_to_row[size]:
                        row = idx
                        break
                curr = row_order.index(row)
                while row_order[ending_position] != row:
                    if curr > ending_position:
                        row_order[curr], row_order[curr-1] = row_order[curr-1], row_order[curr]
                        curr -= 1
                    elif curr < ending_position:
                        row_order[curr], row_order[curr+1] = row_order[curr+1], row_order[curr]
                        curr += 1
                    swaps += 1
                zero_to_row[size].remove(row)
                if (size-1) in zero_to_row:
                    zero_to_row[size-1] += zero_to_row[size]
                else:
                    zero_to_row[size-1] = zero_to_row[size]
                ending_position += 1
            except:
                # no solution
                return -1
        return swaps

             
test = Solution()   
print(test.minSwaps([[1,0,0,0],[1,0,0,0],[1,1,0,0],[0,1,0,0]])) # 0
print(test.minSwaps([[0,1,1,0],[1,1,1,0],[1,1,1,0],[1,0,0,0]])) # -1
print(test.minSwaps([[1,1],[1,0]])) # 1
print(test.minSwaps([[0,0,0,0,0,1],[0,0,0,0,1,0],[0,0,0,1,0,0],[0,0,1,0,0,0],[0,1,0,0,0,0],[1,0,0,0,0,0]])) # 15
print(test.minSwaps([[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,1]])) # 4
print(test.minSwaps([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]])) # 2
print(test.minSwaps([[1,0,0],[1,1,0],[1,1,1]])) # 0
print(test.minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]])) # -1
print(test.minSwaps([[0,0,1],[1,1,0],[1,0,0]])) # 3