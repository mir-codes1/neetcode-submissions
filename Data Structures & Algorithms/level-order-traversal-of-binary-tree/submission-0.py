# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append([root])
        result = []

        if not root:
            return []

        while q:
            nodes = q.popleft()
            wave = []
            result1 = []
            for node in nodes:
                if node.left:
                    wave.append(node.left)
                if node.right:
                    wave.append(node.right)    
            for node in nodes:
                result1.append(node.val)
            result.append(result1)
            if wave:
                q.append(wave)
        return result