class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result

        low = nums[0]
        high = nums[0]
        curr = 1
     
        while curr <= len(nums)-1:
            if nums[curr] == nums[curr-1] + 1:
                high = nums[curr]
            else:
                if(high == low):
                    output = str(high)
                else:
                    output = str(low) + "->" + str(high)
                result.append(output)
                low = nums[curr]
                high = nums[curr]
            curr = curr + 1

        if(high == low):
            output = str(high)
        else:
            output = str(low) + "->" + str(high)
        result.append(output)

        return result

                