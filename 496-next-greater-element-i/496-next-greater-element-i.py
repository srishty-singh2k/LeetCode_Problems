class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack, m = [], {}
        for num in nums2:
            while stack and stack[-1] < num:
                m[stack.pop()] = num
            stack.append(num)
        res = []
        for num in nums1:
            res.append(m.get(num, -1))
        return res