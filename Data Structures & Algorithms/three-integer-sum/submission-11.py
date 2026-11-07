class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = dict()
        result = set()

        for i in range(len(nums)):
            seen[nums[i]] = i
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                target = -(nums[i]+nums[j])

                if target in seen and i != j and i != seen[target] and j != seen[target]:
                    result.add(tuple(sorted((nums[i], nums[j], target))))
        return list(result)