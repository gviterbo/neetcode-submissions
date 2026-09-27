# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def dfs(root, p, ans):
            ans.append(root)
            if root.val == p:
                return ans
            if root.val > p:
                return dfs(root.left, p, ans)
            else:
                return dfs(root.right, p, ans)
        s1 = dfs(root, p.val, [])
        s2 = dfs(root, q.val, [])

        while(len(s1) or len(s2)):
            if len(s1) > len(s2):
                s1.pop()
            elif len(s2) > len(s1):
                s2.pop()
            elif s2[-1] == s1[-1]:
                return s2[-1]
            else:
                s1.pop()
            
                

