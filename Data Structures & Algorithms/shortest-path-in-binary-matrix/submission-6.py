class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        elif grid[0][0] == 1:
            return -1
        elif len(grid) == 1:
            return 1


        visited = set((0, 0))
        count = 0
        q = collections.deque()
        q.append([(0, 0)])
        while q:
            cells = q.popleft()
            neighbors = []
            for r, c in cells:
                directions = [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, -1],
                [-1, 1], [1, -1]]
                
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (row in range(len(grid)) and
                    col in range(len(grid[0])) and 
                    grid[row][col] == 0 and
                    (row, col) not in visited):
                        if (row, col) == (len(grid)-1, len(grid[0])-1):
                            return (count + 2)
                        neighbors.append((row, col))
                        visited.add((row, col))
            if neighbors:
                q.append(neighbors)
                count += 1
        return -1
