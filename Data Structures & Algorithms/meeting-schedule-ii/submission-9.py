"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()

        a = b = 0
        count = largest = 0

        for _ in intervals:
            if starts[a] < ends[b]:
                count += 1
                largest = max(largest, count)
                a += 1
            elif starts[a] >= ends[b]:
                count -= 1
                b += 1
        return largest
