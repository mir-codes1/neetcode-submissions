class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running, largest = 0, nums[0]
        
        for num in nums:
            if running < 0:
                running = 0
            running += num
            largest = max(running, largest)            

        return largest