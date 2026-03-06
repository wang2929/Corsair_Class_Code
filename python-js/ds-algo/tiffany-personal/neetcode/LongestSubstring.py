'''
Given a string s, find the length of the longest substring without duplicate characters.
(Sliding window)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0  
        start, end = 0, 1
        max_len = 1
        seen = s[start]
        while start < end and end < len(s):
            if s[start] == s[end]:  # shift the whole window
                end += 1
                start += 1
            elif s[end] in seen:    # shift only the start
                start += 1
            elif s[end] not in seen:    # shift only the end
                max_len = max(max_len, end - start + 1)
                end += 1
            seen = s[start:end]
        return max_len