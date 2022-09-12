class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_prod, min_prod = max(nums[i], max_prod*nums[i], min_prod*nums[i]), min(nums[i], max_prod*nums[i], min_prod*nums[i])             
            
            ans = max(max_prod, ans)
        return ans