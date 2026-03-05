'''
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
Return the minimum number of operations needed to make s alternating.
'''
class Solution:
    def minOperations(self, s: str) -> int:
        # need to try twice, once where the first digit
        # doesn't change and once where it does
        count0 = 0
        count1 = 0
        for i in range(len(s)):
            if i&1 == 0:
                if s[i] == '0':
                    count0 += 1
                else:
                    count1 += 1
            else:
                if s[i] == '1':
                    count0 += 1
                else:
                    count1 += 1
        return min(count0, count1)
    
print(Solution().minOperations("0100"))