# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, arr):
            if node is None:
                return True
            if node.val <= arr[0] or node.val >= arr[1]:
                return False
            
            return dfs(node.left, [arr[0],node.val]) and dfs(node.right, [node.val, arr[1]])

        return dfs(root, [-2000, 2000])
            

            
