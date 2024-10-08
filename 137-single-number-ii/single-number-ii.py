class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        
        for res in result:
            if result[res] == 1:
                return res
            
         