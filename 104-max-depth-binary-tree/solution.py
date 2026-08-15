# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #for each node: figure out the depth so far

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

#same principle:
#each node, needs to calculate the depth of its left and right subtree
#keep going down it
#return 1 + max (left, right)

#Time: O(n) because check each node
#Space: O(n) because recursive stack -> skewed tree