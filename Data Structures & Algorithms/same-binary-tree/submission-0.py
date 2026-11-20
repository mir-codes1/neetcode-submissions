# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        a = collections.deque()
        b = collections.deque()

        a.append(p)
        b.append(q)

        while a and b:
            node1 = a.popleft()
            node2 = b.popleft()


            if node1 and node2 and node1.val != node2.val:
                return False
            if (node1 and not node2) or (not node1 and node2):
                return False

            if node1 and node2:
                a.extend([node1.left, node1.right])
                b.extend([node2.left, node2.right])

        if not a and not b:
            return True
        else:
            return False