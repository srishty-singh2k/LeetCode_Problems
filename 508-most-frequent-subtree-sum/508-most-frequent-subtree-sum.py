# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        def dfs(root):
            
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            ans.append(root.val+left+right)
            
            return root.val+left+right
        
        
        dfs(root)
        
        dic = {}
        
        for i in ans:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
                
        maxim = max(dic.values())
        
        res = []
        
        for i in dic:
            if dic[i]==maxim:
                res.append(i)
                
        return res       
                
                
        
        