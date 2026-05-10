# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, validRange):
            if node is None:
                return True
            if node.val <= validRange[0] or node.val >= validRange[1]:
                return False
            
            return dfs(node.left, [validRange[0],node.val]) and dfs(node.right, [node.val, validRange[1]])

        return dfs(root, [float("-inf"), float("inf")])
            

            
