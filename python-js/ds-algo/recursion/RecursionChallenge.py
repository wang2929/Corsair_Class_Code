class Recursion:
    def __init__(self):
        self.roman_to_number = { "I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
        self.priority = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
    def factorial(self, n):
        if n == 1:
            return 1
        return n*self.factorial(n-1)

    def factorial_iter(self, n):
        ret = 1
        for i in range(1, n+1):
            ret = ret * i
        return ret

    def palindrome_iter(self, word):
        for i in range(len(word)//2):
            if word[i] != word[-(i+1)]:
                return False
        return True

    def palindrome(self, word):
        if len(word) <= 1:
            return True
        if word[0] != word[-1]:
            return False
        return self.palindrome(word[1:-1])
        
    def bottles_song(self, n):
        if n < 0:
            return
        print(f"{n} bottles of beer on the wall. {n} bottles of beer.\nTake one down, pass it around. {n-1} bottles of beer.")
        self.bottles_song(n-1)

    def roman_numerals(self, n, i):
        if n == 0 or i >= len(self.priority):
            return ""
        pri = self.priority[i]
        repeat = n // self.roman_to_number[pri]
        next_n = n - (repeat * self.roman_to_number[pri])
        return pri * repeat + self.roman_numerals(next_n, i+1)
    
    def flatten_list(self, nums):
        if len(nums) == 0:
            return []
        if type(nums[0]) == list:
            return self.flatten_list(nums[0] + nums[1:])
        return [nums[0]] + self.flatten_list(nums[1:])
    
    def binary_search(self, nums, target):
        if len(nums) == 0:
            return -1
        mid = len(nums) // 2
        if target > nums[mid]:
            self.binary_search(nums[mid:])
        elif target < nums[mid]:
            self.binary_search(nums[:mid])
        else:
            return mid

