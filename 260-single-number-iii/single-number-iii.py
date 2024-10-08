class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = {}
        for num in nums:
            if num in result:
                del result[num]
            else:
                result[num] = num
            
        return result
        
        