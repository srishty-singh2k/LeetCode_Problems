class Solution:
    def fillCups(self, amount: List[int]) -> int:
        sum = amount[0] + amount[1] + amount[2]
        res = sum//2+(sum%2)
        if amount[0]>res:
            res += (amount[0]-res)
        elif amount[1]>res:
            res += (amount[1]-res)
        elif amount[2]>res:
            res += (amount[2]-res)
        return res