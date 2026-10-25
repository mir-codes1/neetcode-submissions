class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        # add pacific cells
        for p in range(len(heights)):
            pacific.add((p, 0))
        for p in range(len(heights[0])):
            pacific.add((0, p))

        # add atlantic cells
        for a in range(len(heights)):
            atlantic.add((a, len(heights[0])-1))
        for a in range(len(heights[0])):
            atlantic.add((len(heights)-1, a))
        
        for row, col in pacific.copy():
            q = collections.deque()
            q.append((row, col))
            while q:
                row, col = q.popleft()

                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if (r in range(len(heights)) and
                        c in range(len(heights[0])) and
                        heights[r][c] >= heights[row][col] and
                        (r, c) not in pacific):
                        pacific.add((r, c))
                        q.append((r, c))
        
        for row, col in atlantic.copy():
            q = collections.deque()
            q.append((row, col))
            while q:
                row, col = q.popleft()

                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if (r in range(len(heights)) and
                        c in range(len(heights[0])) and
                        heights[r][c] >= heights[row][col] and
                        (r, c) not in atlantic):
                        atlantic.add((r, c))
                        q.append((r, c))
        
        return list(pacific & atlantic)