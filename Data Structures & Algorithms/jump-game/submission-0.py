class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # for every 0 in the array, can we skip it
        highest = i = 0
        while i < len(nums)-1:
            highest = max(highest, i+nums[i])
            if nums[i] == 0 and highest <= i:
                return False
            i += 1
        return True