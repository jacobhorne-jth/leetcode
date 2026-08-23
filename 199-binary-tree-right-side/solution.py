# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #for each node, is it the rightmost node

        rights = []

        q = deque([root])
        

        while q:
            last = None
            for _ in range(len(q)):
                node = q.popleft()

                if not node:
                    continue

                last = node.val

                q.append(node.left)
                q.append(node.right)

            
            if last or last == 0:
                rights.append(last)
        
        return rights


#basic idea for this was to do level order traversal, store the last seen value and append that to result list
#do this by doing traditional bfs but instead of processing nodes one at at time, use len(queue) to proceses level by level
#keep a var for the last seen value and process each node in that level, adding its children to queue, then appending last if it exists


#Time: O(n)
#Space: O(n) worst case where its one level

        