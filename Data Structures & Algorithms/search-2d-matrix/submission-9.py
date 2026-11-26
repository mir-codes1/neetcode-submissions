class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = 0
        b = len(matrix[0])-1

        def binarySearch(row, a, b):
            while a <= b:
                if matrix[row][a] == target:
                    return True
                if matrix[row][b] == target:
                    return True
                
                center = (a+b)//2
                if matrix[row][center] == target:
                    return True
                elif matrix[row][center] > target:
                    b = center-1
                elif matrix[row][center] < target:
                    a = center+1
            return False


        for row in range(len(matrix)):
            if matrix[row][a] <= target and matrix[row][b] >= target:
                # target is in row
                return binarySearch(row, a, b)
        return False