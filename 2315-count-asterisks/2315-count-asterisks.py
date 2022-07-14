class Solution:
    def countAsterisks(self, s: str) -> int:
        countBar = 0
        countAst = 0
        for each in s:
            if each == '|' :
                countBar += 1
            else:
                if countBar%2 == 0 :
                    if each == '*' :
                        countAst += 1
        return countAst