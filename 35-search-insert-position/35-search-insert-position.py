class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        index=0
        while(index<len(nums) and target>nums[index]):
            index+=1
        
        return index