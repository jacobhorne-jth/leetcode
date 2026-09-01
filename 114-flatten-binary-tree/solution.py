# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #pre order = parent, left, right

        #at each node, append itself, call left, call right


        curr = None


        def helper(node):
            nonlocal curr
            if not node:
                return

            val = node.val
            left, right = node.left, node.right
            
            if curr:
                curr.right = node
                curr.left = None
            
            curr = node
                

            #append

            helper(left)
            helper(right)


        helper(root)


#this one works by remembering tree = what do at each node
#pre order = node, left, right
#so for each node, append self, call helper function on left and right
#as you go, keep track of a curr pointer for the linkedlist
#set curr.right to node and curr.left to None
'''
if there was no curr, set curr = Node

nonlocal = if you create curr outside helper func then in the helper func want to use it
do nonlocal curr at top

then use curr normally

better memory efficient way is to recgonize that each pre order is node then left subtree then right subtree

so move the right subtree to be after the right most value in the left subtree then move it all to the right
and keep doing that as you go down

modifies in place without recrusive stack as you just use a while loop

'''

#Time: O(n) as every node needs to be accessed at least once
#Space: O(h) where h is size of resurive stack, O(1) for more efficient, non recurision solution
