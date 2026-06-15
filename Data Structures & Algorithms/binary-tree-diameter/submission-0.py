# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.height = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxHeight(root):
            if not root:
                return 0

            left, right = maxHeight(root.left), maxHeight(root.right)

            self.height = max(self.height, left + right)

            return 1 + max(left, right)

        maxHeight(root)
        
        return self.height
        