class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest = 0
        for num in piles:
            if num > largest:
                largest = num

        # perform binary search on candidates
        # break condition is when k is minimum
        #   minimum k occurs when k-1 requires hours > h

        def hours_required(k):
            hours = 0
            for bananas in piles:
                hours += -(-bananas // k)
            return hours
        
        k = 0
        a = 1
        b = largest
        while a <= b:
            center = (a + b) // 2
            if hours_required(center) <= h:
                if center == 1 or hours_required(center - 1) > h:
                    return center
                b = center - 1
            else:
                a = center + 1