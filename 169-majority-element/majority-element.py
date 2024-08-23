class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        
    
        nums.sort()  # Sort the list

        majority_count = len(nums) // 2

        count = 1  
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                if count > majority_count:
                    return nums[i - 1]
                count = 1

        # Final check after loop to ensure the last element is handled
        if count > majority_count:
            return nums[-1]

        return 0