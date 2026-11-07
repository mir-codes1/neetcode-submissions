class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        # iterate through intervals
            # if not running then
            #   save curr.start and curr.end as abs_start and abs_end
            #   running = true
            # if running then
            #   if curr.start <= abs_end
            #       abs_end = curr.end
            #   elif curr.start > abs_end
            #       result.append((abs_start, abs_end))
            #       save curr.start and curr.end as abs_start and abs_end
            #       running = true
        # return result
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

        