class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firstMax = secondMax = thirdMax = None
        
        for num in nums:
            # Skip if the number is already used as one of the maxes
            if num == firstMax or num == secondMax or num == thirdMax:
                continue
            
            # Update the three maximums
            if firstMax is None or num > firstMax:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = num
            elif secondMax is None or num > secondMax:
                thirdMax = secondMax
                secondMax = num
            elif thirdMax is None or num > thirdMax:
                thirdMax = num
        
        # Return thirdMax if it exists, otherwise return firstMax
        return thirdMax if thirdMax is not None else firstMax
