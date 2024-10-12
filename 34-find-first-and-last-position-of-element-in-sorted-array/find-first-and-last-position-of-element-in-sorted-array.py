class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid  # Found target, but search left for the first occurrence
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last = mid  # Found target, but search right for the last occurrence
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        # Find the first and last occurrences
        first = findFirst(nums, target)
        last = findLast(nums, target)

        return [first, last]'''

        if not nums:  # Handle empty input
            return [-1, -1]

        left, right = 0, len(nums) - 1
        result = [-1, -1]  # Default result if target not found

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                # Found the target, now expand to both sides
                start, end = mid, mid

                # Expand left to find the first occurrence
                while start > 0 and nums[start - 1] == target:
                    start -= 1

                # Expand right to find the last occurrence
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1

                return [start, end]

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result