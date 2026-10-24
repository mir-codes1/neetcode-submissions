class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # approach:
        #   1. sort by start time
        #   2. iterate checking if next interval conflicts prev:
        #   3.      if conflict then count += 1
        #   4. return count

        intervals.sort(key=lambda i: i[0])
        count = 0
        prev_end = float('-inf')
        for interval in intervals:
            if prev_end > interval[0]:
                # conflict found
                count += 1
                prev_end = min(prev_end, interval[1])
            else:
                prev_end = interval[1]
        return count