# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #at each node, check if it matches subRoot, then go down til end

        #separate the responsibilites
        #check potential starting points : where u return true if it is valid one
        #also function to actually check the entire tree

        def sameTree(node, check):
            if not node and not check:
                return True

            if not node or not check:
                return False

            if node.val != check.val:
                return False

            return sameTree(node.left, check.left) and sameTree(node.right, check.right)



        def search(node):
            if not node:
                return False

            if sameTree(node, subRoot):
                return True

            return search(node.left) or search(node.right)

        return search(root)
        '''
        def checkNode(node, check):
            if not node and not check:
                return True
            
            if not node or not check:
                return False
            
            if node.val == check.val:
                return checkNode(node.left, check.left) and checkNode(node.right, check.right)



            else:
                return checkNode(node.left, check) or checkNode(node.right, check)

        


        return checkNode(root, subRoot)
        '''

#remember: at each node, need to check if its matching a node in the subroot
#do this by having a funciton for sameTree, takes the roots and goes down them
#returns False when they dont match, uses and to make sure both subtrees match

#have a separate function to see if each node is a valid starting place
#if not node: return False
#check sameTree for node and subRoot
#sameTree does its logic, if true, found = return True

#otherwise keep going but this time use or cause it could be down either one

#Time: O(n * m) worst case
#check all n nodes with each can call sameTree which compares up to m nodes so m * n

#Space: O(h_root + h_sub) = recrusive call stack worst case
#search can have up to h_root calls on the stack, sameTree can add up to h_sub more

