class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = 0
        global_max = float('-inf')
        
        for i in range(len(nums)):
            local_max = max(nums[i], nums[i]+local_max)
            if local_max > global_max:
                global_max = local_max
                
        return global_max