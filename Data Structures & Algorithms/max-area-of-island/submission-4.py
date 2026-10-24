class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # go cell by cell:
        # if cell == "1":
        #       run bfs:
        #           everytime a cell is marked as visited, count += 1
        # max(count, largest)
        # count = 0

        largest = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            count = 0
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                cr, cc = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    row, col = cr + dr, cc + dc
                    if (row in range(rows) and
                        col in range(cols) and
                        grid[row][col] == 1 and
                        (row, col) not in visited):
                        q.append((row, col))
                        visited.add((row, col))
                count += 1
            return count


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    count = bfs(r, c)
                    largest = max(count, largest)

        return largest