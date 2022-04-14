class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            c=target-nums[i]
            if c in nums and i!=nums.index(c):
                return [i,nums.index(c)]
            
                    
        