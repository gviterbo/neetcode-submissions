# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def bfs(root):
            nonlocal ans
            q = deque([root])

            while(q):
                temp = []
                for x in q:
                    temp.append(x.val)
                ans.append(temp)
                n = len(q)
                for _ in range(n):
                    node = q.popleft()
                    if node.left: 
                        q.append(node.left)
                    if node.right: 
                        q.append(node.right)
        bfs(root)
        return ans


                    
