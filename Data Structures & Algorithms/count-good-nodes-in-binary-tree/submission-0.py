# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        if root.left is None and root.right is None:
            return 1
        
        def dfs(node, max_value):
            if not node:
                return 

            if node.val >= max_value:
                self.ans += 1
                max_value = node.val
            dfs(node.left, max_value)
            dfs(node.right, max_value)
        
        dfs(root, -200)
        return self.ans