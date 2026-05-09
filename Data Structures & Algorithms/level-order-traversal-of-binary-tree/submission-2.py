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
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            num = len(queue)
            curr_lvl = []
            for _ in range(num):
                node = queue.popleft()
                curr_lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(curr_lvl)
        return ans


## DFS Solution ##            
        # ans = [[root.val]]
        # stack = []
        # if root.right: stack.append((root.right, 1))
        # if root.left: stack.append((root.left, 1))
        # while stack:
        #     node, i = stack.pop()
        #     if i == len(ans):
        #         ans.append([])
        #     ans[i].append(node.val)
        #     if node.right: stack.append((node.right, i+1))
        #     if node.left: stack.append((node.left, i+1))  
        # return ans

