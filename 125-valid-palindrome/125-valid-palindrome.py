class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for c in s:
            if c.isalpha():
                new += c.lower()
            elif c.isdigit():
                new += c
        print(new)
        if len(new)%2 == 0:            
            return new[:len(new)//2] == new[-1:len(new)//2-1:-1]
        return new[:len(new)//2] == new[-1:len(new)//2:-1]