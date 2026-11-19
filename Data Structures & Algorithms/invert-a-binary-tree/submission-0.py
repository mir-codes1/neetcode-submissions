# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # dfs, swap children and append each to queue

        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()

            if node and (node.left or node.right):
                temp = node.left
                node.left = node.right
                node.right = temp

                q.append(node.left)
                q.append(node.right)
        return root