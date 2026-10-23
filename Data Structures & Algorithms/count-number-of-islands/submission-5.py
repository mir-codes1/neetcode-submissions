class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        seen = set()

        def bfs(r, c):
            q = collections.deque()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            seen.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    if ((dr + row) in range(len(grid)) and
                        (dc + col) in range(len(grid[0])) and
                        ((dr + row), (dc + col)) not in seen and
                        grid[dr + row][dc + col] == "1"):
                        q.append((dr + row, dc + col))
                        seen.add((dr+row, dc + col))


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    islands += 1
        return islands