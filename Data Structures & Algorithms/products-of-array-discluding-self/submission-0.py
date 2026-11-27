class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prev = 1
        length = len(nums)
        for num in nums:
            prefix.append(num*prev)
            prev = num*prev
        
        postfix = [0] * length
        prev = 1
        for i in range(length-1, -1, -1):
            postfix[i] = nums[i] * prev
            prev = nums[i] * prev
        
        result = [0] * length
        for i in range(length):
            if i == 0:
                result[i] = postfix[i+1]
            elif i == length-1:
                result[i] = prefix[i-1]
            else:
                result[i] = prefix[i-1] * postfix[i+1]
        return result