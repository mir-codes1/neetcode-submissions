class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_oranges = 0
        mins_passed = 0
        rotted = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num_oranges += 1
                elif grid[i][j] == 2:
                    rotted.append((i, j))
        
        q = collections.deque()
        q.append(rotted)
        while q:
            rotted = q.popleft()
            to_rot = []

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for orange in rotted:
                for dr, dc in directions:
                    row = orange[0] + dr
                    col = orange[1] + dc
                    if (row in range(len(grid)) and
                    col in range(len(grid[0])) and
                    grid[row][col] == 1):
                        to_rot.append((row, col))
                        grid[row][col] = 2
                        num_oranges -= 1
            
            if to_rot:
                mins_passed += 1
                q.append(to_rot)
        
        if num_oranges > 0:
            return -1
        elif num_oranges == 0:
            return mins_passed