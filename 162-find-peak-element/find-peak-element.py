class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        array_size = len(nums)
        
        # Handle edge cases for array size less than 3
        if array_size == 1:
            return 0
        
        if array_size == 2:
            return 0 if nums[0] > nums[1] else 1

        for i in range(1, array_size - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
            
        # last element
        if nums[-1] > nums[-2]:
            return array_size - 1

        # first element
        if nums[0] > nums[1]:
            return 0
            
        
        