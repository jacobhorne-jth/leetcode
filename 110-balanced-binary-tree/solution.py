# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0

            lh = height(node.left)
            if lh == -1:
                return -1

            rh = height(node.right)
            if rh == -1:
                return -1

            if abs(rh - lh) > 1:
                return -1

            return 1 + max(lh, rh)



        return height(root) != -1


"""
basic idea for this is do dfs on each node
go down to the bottom, each one comparing left and right nodes
#if different in height is found to be -1 at any point, bring that -1 all the way up
base case, as usually: if not node: return 0

and if none of those, return 1 + max(lh, rh)
#that way the true height of each node is reflected if its uneven

Time: O(n) where n = number of nodes because each node is visited at most once
Space: O(h) where h = height of the tree, due too recrusive call stack
balanced: O(logn), O(n) when skewed tree

"""