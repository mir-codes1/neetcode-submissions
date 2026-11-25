# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # left child is smaller than current node
        # right child is greater than current node

        # traverse through tree
        # break condition = (currNode.left > p or currNode.left > q) and (currNode.right < p or currNode.right < q)

        queue = collections.deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()

            if (q.val <= curr.val and p.val >= curr.val) or (p.val <= curr.val and q.val >= curr.val):
                return curr
            elif q.val > curr.val and p.val > curr.val:
                queue.append(curr.right)
            elif q.val < curr.val and p.val < curr.val:
                queue.append(curr.left)
