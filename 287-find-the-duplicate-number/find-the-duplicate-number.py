class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            if num in result:
                return num
            else:
                result[num] = num
        return 0
        
        