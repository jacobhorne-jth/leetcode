# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


#key idea here is to remember to just look at what each node needs to do
#here each node just needs to reverse its children (swap it)

#Time: O(n) because it visits every node
#Space: O(n) worst because recursive stack for a skewed tree