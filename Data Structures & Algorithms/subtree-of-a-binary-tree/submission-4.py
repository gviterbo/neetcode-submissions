# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def equal(t1, t2) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val == t2.val:
                return equal(t1.left, t2.left) and equal(t1.right, t2.right)
            else:
                return False

        
        def dfs(t1, t2) -> bool:
            if not t1:
                return False
            
            return dfs(t1.left,t2) or dfs(t1.right,t2) or equal(t1, t2)
        return dfs(root, subRoot)