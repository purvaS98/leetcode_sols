class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        op = 0
        for res in result:
            if result[res] == 2:
                op = op ^ res
            
        return op 
        

        