# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        depths = {None: 0}

        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                depths[node] = 1 + max(depths[node.left], depths[node.right])
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return depths[root]