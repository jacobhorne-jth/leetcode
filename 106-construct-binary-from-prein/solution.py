# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        #inorder = left, node, right
        #postorder = left, right, node

        indexing = {val: i for i, val in enumerate(inorder)}

        def build(left, right):
            if left > right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            mid = indexing[root_val]

            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            

            return root

        return build(0, len(inorder) - 1)
            
        
#use the fact that the end of the postorder list = the root
#and then use in order to split it
#find the end of postorder element in inorder and then realize to the left is the left subtree, to the right is the right subtree
#at each step find this and use it to build each subtree

#use a helper that takes the left and right bounds
#also take the indexes of the inorder for use later (used to separate subtrees)

'''
start by calling the build helper on 0 and last index of in order as the left and right bounds
#edge case = left > right (return None to break)
then calccualte the root val from popping from postorder then create root with TreeNode(rootval)
#IMPORTANT
because post order roots go from most right to left, the next end of postorder will be the right subtrees root
so you have to do the entire right subtree first (build right first)

once root.left + root.rigth are set to build(), return root


Time: O(n) where n is number of nodes
Space: O(n) for the indexing dict created for finding out where in inorder you are
also O(n) because of worst case recrusive stack (skewed tree, all on one side)
'''