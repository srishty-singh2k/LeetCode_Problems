class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        if target in nums:
            res[0]=nums.index(target)
            res[1]=len(nums)-(nums[::-1].index(target))-1
        return res