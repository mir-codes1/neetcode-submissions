# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def trees_are_equal(curr_node):
            a = collections.deque()
            b = collections.deque()

            a.append(curr_node)
            b.append(subRoot)
            while a and b:
                node1 = a.popleft()
                node2 = b.popleft()
                if not node1 and not node2:
                    continue
                    
                if (not node1 and node2) or (node1 and not node2) or (node1.val != node2.val):
                    return False

                a.append(node1.left)
                a.append(node1.right)
                b.append(node2.left)
                b.append(node2.right)
            return True


        q = collections.deque()
        candidates = []
        q.append(root)
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                candidates.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        for candidate in candidates:
            if trees_are_equal(candidate):
                return True
        return False