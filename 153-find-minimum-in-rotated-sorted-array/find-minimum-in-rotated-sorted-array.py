class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Initialize the pointers
        left = 0
        right = len(nums) - 1
        
        # If the array is not rotated (the smallest element is the first one)
        if nums[right] > nums[0]:
            return nums[0]

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2

            # Check if mid element is smaller than its previous element
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            # Check if mid+1 element is the smallest
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            # Decide which half to continue with
            if nums[mid] >= nums[left]:  # Left part is sorted
                left = mid + 1
            else:  # Right part is sorted
                right = mid - 1

        # In case no return happens within the loop, return -1 (error condition)
        return -1
        