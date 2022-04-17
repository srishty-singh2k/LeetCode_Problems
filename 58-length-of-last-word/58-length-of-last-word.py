class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s=="":
            return 0
        words=list(s.split(" "))
        while "" in words:
            words.remove("")
        return len(words[-1])