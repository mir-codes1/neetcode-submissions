class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # queue a list of neighbors at a time rather than one neighbor at a time

        q = collections.deque()
        rotted = []
        n_oranges = 0
        mins_passed = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    n_oranges += 1
                elif grid[i][j] == 2:
                    rotted.append((i, j))
        q.append(rotted)
        while q:
            rotted = q.popleft()
            to_rot = []

            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for r, c in rotted:
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (row in range(len(grid)) and
                    col in range(len(grid[0])) and
                    grid[row][col] == 1):
                        to_rot.append((row, col))
                        grid[row][col] = 2
                        n_oranges -= 1
            if to_rot:
                mins_passed += 1
                q.append(to_rot)
            

        if n_oranges > 0:
            return -1
        elif n_oranges == 0:
            return mins_passed