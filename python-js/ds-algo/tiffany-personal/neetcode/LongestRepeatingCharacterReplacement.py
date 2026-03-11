'''
You are given a string s consisting of only uppercase english characters and an integer k. 
You can choose up to k characters of the string and replace them with any other uppercase English character.
After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
'''
class Solution:
    '''
    Problem: want to find longest substring given k replacements
    Example: AAABABB, 1 -> len("AAAAABB") = 5
            AABBBAA, 3 -> len("AAAAAAA") = 7
    Data Structure:
    Algorithm:
        1) set l, r to the start
        2) move r out and expand window until k replacements makes a longer substring
        3) move l and measure again
        4) return the longest substring
    How to track? I don't know
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        ret = 0
        tracker = {}
        tracker[s[l]] = tracker.get(s[l], 0) + 1
        tracker[s[r]] = tracker.get(s[r], 0) + 1
        while True:
            max_char = max(tracker, key=lambda k: tracker[k])
            other_chars = sum(tracker.values()) - tracker[max_char]
            if s[l:(r+1)].count(s[l]) == (r - l + 1) or other_chars <= k:
                ret = max(ret, r - l + 1)
                r += 1
                if r == len(s): break
                tracker[s[r]] = tracker.get(s[r], 0) + 1
            else:
                tracker[s[l]] = tracker.get(s[l], 0) - 1
                l += 1
                if l == r:
                    r += 1
                    if r == len(s): break
                    tracker[s[r]] = tracker.get(s[r], 0) + 1
        return ret

print(Solution().characterReplacement("AAAA", 0)) # 4
print(Solution().characterReplacement("ABAA", 0)) # 2
print(Solution().characterReplacement("XYYXXY", 2)) # 5
print(Solution().characterReplacement("AAABABB", 1)) # 5