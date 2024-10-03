class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        res = 0
        n = len(nums)

        for i in range(len(nums)):
            sum = sum + nums[i]
            
        res = n * (n + 1) // 2
            
        return res - sum


        