class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        occurences = defaultdict(int)

        for num in nums:
            occurences[num] += 1
        
        for key, value in occurences.items():
            buckets[value].append(key)
        
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result