# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        q = collections.deque()
        if root:
            q.append((root, 1))
        largest = 0
        while q:
            popped = q.popleft()
            node = popped[0]
            depth = popped[1]
            
            largest = max(largest, depth)

            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))

        return largest