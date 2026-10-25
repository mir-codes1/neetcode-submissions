class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest = 0
        q = collections.deque()
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == 1:
                    q.append((row, col))
                    count = 0
                    while q:
                        r, c = q.popleft()
                        if (r, c) not in visited:
                            visited.add((r, c))
                            count += 1

                            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                            for dr, dc in directions:
                                cr = r + dr
                                cc = c + dc
                                if (cr in range(len(grid)) and
                                    cc in range(len(grid[0])) and
                                    grid[cr][cc] == 1 and
                                    (cr, cc) not in visited):
                                    q.append((cr, cc))
                    
                    largest = max(count, largest)
                    count = 0
        return largest