# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Precompute indices for O(1) partition lookups
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            # Base case: no elements left in this subtree
            if in_left > in_right:
                return None

            # Current root is always next available in preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Split inorder into left and right subtrees
            mid = inorder_map[root_val]

            # Build left subtree first because preorder is (Root -> Left -> Right)
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)