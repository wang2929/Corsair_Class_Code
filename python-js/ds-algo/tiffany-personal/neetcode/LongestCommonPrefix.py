class Solution:
    '''
    PEDAC - Problem, examples, data structure, algorithm, code
    Problem: Find longest prefix
    Examples: given
    Data Structure: string for the prefix
    Algorithm: 
        no words:
            return ""
        one word:
            return word
        more than one word: compare two words
            If letters don't match, return longest prefix
            Return the min of matching prefixes
        Special cases:
            word length is 0: return ""
            word length is 1: return either word or ""
        Notes:
            Can use the shortest word as the prefix to compare
            Try to quit early if prefix is ""
    '''
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        strs = sorted(strs, key=len)
        prefix = strs[0]
        for i in range(1, len(strs)):
            if len(prefix) == 0: 
                return prefix
            idx = 0
            for idx in range(len(prefix)):
                if prefix[idx] != strs[i][idx]:
                    idx -= 1
                    break
            prefix = min(prefix, strs[i][:idx+1]) 
        return prefix