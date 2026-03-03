'''
Given two positive integers n and k, the binary string Sn is formed as follows:
    S1 = "0"
    Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
For example, the first four strings in the above sequence are:
    S1 = "0"
    S2 = "011"
    S3 = "0111001"
    S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.
'''
class Solution:
    def __init__(self):
        self.bin_pat = ["0", "011", "0111001", "011100110110001"]
    def findKthBit(self, n: int, k: int) -> str:
        for i in range(len(self.bin_pat), n):
            inv = ''.join(['1' if j == '0' else '0' for j in self.bin_pat[-1]])
            new_entry = self.bin_pat[-1] + '1' + inv[::-1] # reverse the inverse
            self.bin_pat.append(new_entry)
        return self.bin_pat[n-1][k-1]
    
test = Solution()
print(test.findKthBit(5, 24)) # 0
print(test.findKthBit(4, 11)) # "011100110110001", 11th bit is 1
print(test.findKthBit(3, 1)) # "0111001", 1st bit is 0