class Solution:
    # find the longest repeat sequence and flip it to two odd partitions
    def minFlips(self, s: str) -> int:
        temp, start = 0, -1
        longest, curr_length = 0, 0
        if s[0] == s[-1]:
            # count from start to end
            start_len, end_len = 0, 0
            for i in range(1, len(s)):
                if s[i-1] != s[i]:
                    start_len = i
                    break
            for i in range(len(s)-1, 0, -1):
                if s[i-1] != s[i]:
                    end_len = len(s) - i
                    break
            longest = start_len + end_len
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                curr_length += 1
                if (curr_length + 1) > longest:
                    start = temp
                    longest = curr_length + 1
            else:
                temp = i
                curr_length = 0
        # perform removes as many times as longest
        if start >= 0:
            index = start + (longest // 2 if longest&1 == 1 else longest // 2 - 1)
            s_list = list(s[index:] + s[:index])
        else:
            s_list = list(s)
        flips = 0
        for i in range(1, len(s)):
            if s_list[i] == s_list[i-1]:
                flips += 1
                s_list[i] = str(1 - int(s_list[i]))
        return flips
print(Solution().minFlips("111000"))
print(Solution().minFlips("11100000111"))