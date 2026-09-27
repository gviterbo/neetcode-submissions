# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([root])
        ans = 1
        while(q):
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    if node.left.val < node.val:
                        node.left.val = node.val
                    else: ans += 1
                    q.append(node.left)
                if node.right:
                    if node.right.val < node.val:
                        node.right.val = node.val
                    else: ans += 1

                    q.append(node.right)
        return ans

        