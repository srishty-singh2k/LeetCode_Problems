class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=1
        while(index<=(len(nums)-1)):
            if nums[index-1]==nums[index]:
                nums.pop(index)
                print(index)
            else:
                index+=1
                
        return len(nums)