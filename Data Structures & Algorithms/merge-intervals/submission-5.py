class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        
        running = False
        abs_start, abs_end = 0, 0
        result = []
        for curr in intervals:
            if not running:
                abs_start = curr[0]
                abs_end = curr[1]
                running = True
            elif running:
                if curr[0] <= abs_end:
                    abs_end = max(curr[1], abs_end)
                elif curr[0] > abs_end:
                    result.append((abs_start, abs_end))
                    abs_start = curr[0]
                    abs_end = curr[1]
        result.append((abs_start, abs_end))
        return result

        