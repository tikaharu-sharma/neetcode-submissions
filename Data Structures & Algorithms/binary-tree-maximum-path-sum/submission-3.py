# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val 

        def dfs(node):
            if not node:
                return 0
            
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            
            left_val = max(0, left_val)
            right_val = max(0, right_val)

            self.max_sum = max(self.max_sum, node.val+left_val+right_val)

            return node.val + max(left_val, right_val)
        
        dfs(root)
        return self.max_sum

        
