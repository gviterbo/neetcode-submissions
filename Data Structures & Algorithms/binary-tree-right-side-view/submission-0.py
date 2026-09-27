# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = deque([root])
        res = []
        while ans:
            res.append(ans[-1].val)
            for _ in range(len(ans)):
                node = ans.popleft()
                if node.left: 
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
        return res
