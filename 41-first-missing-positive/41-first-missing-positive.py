class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = {}
        for i in range(1, len(nums)+1):
            d[i] = True
            
        for each in nums:
            if each in d:
                del d[each]
        
        if len(d)>0:
            return list(d.keys())[0]
        return len(nums)+1
            
        