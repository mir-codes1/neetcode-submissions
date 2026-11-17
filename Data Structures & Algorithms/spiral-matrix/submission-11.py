class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return [matrix[0][0]]
            
        rows, cols = len(matrix), len(matrix[0])
        num_of_nodes = rows * cols
        result = []
        r = c = num_of_visited = direction = 0
        visited = set()
        
        while num_of_visited < num_of_nodes:
            # move right (column increases up to cols - 1)
            while direction == 0 and c < cols - 1 and (r, c + 1) not in visited:
                result.append(matrix[r][c])
                visited.add((r, c))
                num_of_visited += 1
                c += 1

            # move down (row increases up to rows - 1)
            while direction == 1 and r < rows - 1 and (r + 1, c) not in visited:
                result.append(matrix[r][c])
                visited.add((r, c))
                num_of_visited += 1
                r += 1

            # move left (column decreases down to 0)
            while direction == 2 and c > 0 and (r, c - 1) not in visited:
                result.append(matrix[r][c])
                visited.add((r, c))
                num_of_visited += 1
                c -= 1

            # move up (row decreases down to 0)
            while direction == 3 and r > 0 and (r - 1, c) not in visited:
                result.append(matrix[r][c])
                visited.add((r, c))
                num_of_visited += 1
                r -= 1

            direction = (direction + 1) % 4

            if num_of_visited == num_of_nodes - 1:
                result.append(matrix[r][c])
                visited.add((r, c))
                num_of_visited += 1
                
        return result