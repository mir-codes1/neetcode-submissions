class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums)-1

        while a <= b:
            center = (a+b)//2
            if nums[a] == target:
                return a
            if nums[b] == target:
                return b

            if nums[center] == target:
                return center
            elif nums[center] > target:
                b = center-1
            elif nums[center] < target:
                a = center+1
        return -1